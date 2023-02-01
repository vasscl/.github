# Init containers alternative to environment configuration

When using **hardened images** in order to deploy your applications as docker containers, you will probably find the issue of having an image that doesn't have any other software installed other than the runtime environment your application needs.

So if you need helpers to load your environment config like **Consul-template** you wont be able to use it inside that image.Therefore in order to load environment variables configuration at **runtime** you have 2 options:

- Your application loads environment variables as part of the boot process of the system,so you will need to code that in your project.
- Your application is already provided with environment variables pre loaded before execution.

In this guide we are going to go over a solution for the 2nd option for our Cencosud X deployment environment.

## Using init containers

When using kubernetes to deploy your application, there is configuration resource of Pods called **init containers** with allows us to run code before our actual application container is created, for more info read [documentation](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/).

In this example we are going to over a solution for a nodejs application loading environment variables form consul using consul-template.

### Consul template as a kubernetes [Configmap]

First we need to set our consul-template configuration has a Configmap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-consul-config
  namespace: my-app-ns
data:
  env.tmpl: |
    {{key (print "app-domain/my-app/" (env "ENVIRONMENT") "/.env")}}

  config.hcl: |
    consul {
      retry {
        enabled     = true
        attempts    = 3
        backoff     = "50ms"
        max_backoff = "10s"
      }
    }

    log_level = "info"

    template {
      source      = "./templates/env.tmpl"
      destination = "./config/.env"
      perms       = 0644
      backup      = false
    }
```

### Configuring init container inside our deployment

Now configure in our deployment manifest our init container that will run over a consul-template image and perform our environment configuration

```yaml
...
replicas: 1
  template:
    spec:
      volumes:
        - name: consul-config
          configMap:
            name: app-consul-config
        - name: env-config
          emptyDir: {}

      initContainers:
        - name: consul-env-loader
          image: hashicorp/consul-template
          env:
            - name: ENVIRONMENT
              value: 'staging'
            - name: CONSUL_HTTP_TOKEN
              valueFrom:
                secretKeyRef:
                  name: consul-token-secret
                  key: token
          args: [
            "-log-level",
            "info", "-once",
            "-config",
            "./templates/config.hcl",
            "-consul-addr",
            "https://consul.tools.cencox.xyz"
          ]
          volumeMounts:
          - name: consul-config
            mountPath: "/templates"
          - name: env-config
            mountPath: "/config"

      containers:
        - name: my-app
          image: us.gcr.io/vasscl/my-app:latest
          volumeMounts:
            - name: env-config
              mountPath: /home/app/config
...
```

## Important notes

- Make sure your are referencing the exact name of the Configmap
- Be careful about the volumes created and mounted inside the initContainer and our main container, this is the way we are sharing configuration between containers
- When configuring CONSUL_HTTP_TOKEN has an environment variable note we are taking it from a secret, make sure you are not sharing this secret on any file https://kubernetes.io/docs/concepts/configuration/secret/


## Conclusions

The use of this solution allows us to keep some good practices recommended in https://12factor.net/es/ in the process of deploying our applications like:

- Keeping immutable images between environments. Because our image doesn't holds any configuration options embedded or compiled in.
- Our environment is loaded on execution time, so we don't have to modify deployment pipelines in order to configure this.
