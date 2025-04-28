job "postgres" {
  datacenters = ["dc1"]
  type = "service"

  group "db" {
    task "postgres" {
      driver = "exec"

      config {
        command = "/usr/lib/postgresql/15/bin/postgres"
        args = [
          "-D", "/tmp/pgdata",   # Data directory (init required before run)
          "-p", "5432"
        ]
      }

      resources {
        cpu    = 500
        memory = 512
        network {
          port "db" {
            to = 5432
          }
        }
      }

      # Optional: Set env variables if needed
      env {
        PGDATA = "/tmp/pgdata"
      }

      # Optional: Init script (only runs once manually before starting the job)
      # Or use "template + artifact" to automate it
    }
  }
}
