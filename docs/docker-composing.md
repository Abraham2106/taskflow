# Docker Composing
A brief overview of Docker and how to create dockerfiles. This research aligns with my college curriculum, making it a valuable skill for both academic and professional development.
[Source](https://www.hostinger.com/tutorials/docker-tutorial)
## Concepts 

* Containerization  
OS level virtualization that packages apps to run in isolated user spaces called containers.   
A container bundles an app with all its necessary components - code, sys libs, dependencies  
and config files - to create an isolated environment.  
Benefits:  

    - Portability: Containers run consistently on any environment. Eliminates the compatibility issues when moved to different systems. 
    - Efficiency: Containers have fewer requirements than VMs. Making them more lightweight.  
    - Isolation: Each container runs isolated preventing conflicts between the apps.  

* Docker Engine  
Docker Engine is the core for building and containerizing apps. It uses a client-server  
architecture to manage all Docker objects, such as images, containers & networks.
Main parts of a Docker Engine: 
    - The server: A long-runnig daemon process ( dockerd ) that handles all the important tasks. CRUD of the engine.
    - APIs: Interfaces that allow programs, such as Docker CLI to communicate with and instruct the daemon.  
    - The CLI client: The Docker CLI that is the primary way to interact with the platform. 

* Docker Hub
It hosts official images for popular software. Tags are used to label and id images.

* Docker images: 

    A docker image is a read-only template that contains a set of instructions and files needed to  
    create a Docker container. 
    Images are different that Dockerfiles, the images are created from the docker files  
    Images are an immutable layer that defines what an image should contain or do. 
    An image is the blueprint for the creation of the container. It can´t be changed once built. 

* Docker Containers:

    A container is a runnable instance of an image. A writable layer is added on top of the image´s read-only layer.  
    Allowing modification in its local filesystem.  
    Containers are stateless, they can be stopped, destroyed, rebuilt with minimal configuration.  
    An individual container is managed with Docker CLI, while multiple ones are administered   
    using **Docker Compose** or an orchestration tool like Kubernetes.  
    A container is created using the image.  
    To run a docker Container use:  
    ```bash
    > docker run -it ubuntu /bin/bash 
    ```

* Dockerfiles:  

    A **Dockerfile** is a plain text file that contains a sequence of step-by-step instructions  
    for building a Docker Image. It defines everything from the base OS to the env vars and app code.  
    Common Key Instructions:  
    ```bash
    FROM                # -> Base Image for the build stage
    RUN                 # -> Executes command during the image build process 
    COPY || ADD         # -> Copies files from the build context into the image
    CMD || ENTRYPOINT   # -> Defines the command that runs when the container starts 
    ENV                 # -> Sets environment variables that will be available during the build and at runtime
    WORKDIR             # -> Sets the working directory for all of the instructions above except ENV. & FROM
    ```

    Some Dockerfile instructions create a layer - a step into the image build process.   
    Some instructions that set config or metadata don't such as `WORKDIR`.

    Dockerfile Example:  
    ```yml
    FROM python:3.9-slim
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    CMD ["python", "app.py"]
    ```

* Docker Compose:

    **Docker Compose** is a tool that simplifies the definition and management of multi-container apps using a single configuration file   
    typically named ```docker-compose.yml```.  
    Within the config file, devs can define all the containers, networks, and volumes to build a complex application stack.  
    The containers now can be administered in the context of Docker Compose with a single command.  
    Without Docker Compose every container has to be managed separately using Docker CLI.  
    ```yml
    services:
        web:
            build: ./web  # Build the image from Dockerfile in the ./web directory
            ports:
            - "8000:8000"  # Map host port 8000 to container port 8000
            depends_on:
            - db     # Wait for the db service to be started
            - redis  # Wait for the redis service to be started

        db:
            image: postgres:15  # Use the official PostgreSQL 15 image
            environment:
            POSTGRES_USER: myuser       # Set database username
            POSTGRES_PASSWORD: mypassword  # Set database password
            POSTGRES_DB: mydb           # Set initial database name
            volumes:
            - db-data:/var/lib/postgresql/data  # Persist database data using a named volume

        redis:
            image: redis:alpine  # Use a lightweight Redis image for caching

    volumes:
        db-data:  # Define a named volume to store database data
    ```  
    To build and start all the services defined in your docker-compose.yml run with the -d command.  
    ```bash
    docker compose up -d
    ```


> docker-compose.yml
```yml
services: 
    web:
        build: ./simple-website
        ports:
        - "8000:8000" 
        depends_on:
        - db
    
    db: 
        image: postgres:15 
        environment:
        POSTGRES_USER: myuser           # Set database username
        POSTGRES_PASSWORD: mypassword   # Set database password
        POSTGRES_DB: mydb               # Initial Database Name
        volumes:
        - db-data:/var/lib/postgresql/data 
    
volumes:
    db-data: # Named volume 
```

```yml
FROM node:20
WORKDIR /simple-website
COPY package.json package-lock.json ./
RUN npm install
COPY . . 
CMD ["node", "index.js"]

```
base de dato postgres y backend con imagen personalizada de node.js 

## Docker Commands Reference Guide

### Docker CLI Commands

#### Image Management
| Command | Flags | Description |
|---------|-------|-------------|
| `docker build` | `-t <name>` | Build an image from a Dockerfile and tag it |
| | `-f <dockerfile>` | Specify a different Dockerfile path |
| | `--no-cache` | Build without using cached layers |
| `docker pull` | N/A | Download an image from Docker Hub |
| `docker push` | N/A | Upload an image to Docker Hub |
| `docker images` | `-a` | List all images (including dangling images) |
| | `--filter "dangling=true"` | Show only unused images |
| `docker rmi` | `-f` | Remove image (force if in use) |
| `docker tag` | `<image:tag> <new-image:tag>` | Create a new tag for an image |

#### Container Management
| Command | Flags | Description |
|---------|-------|-------------|
| `docker run` | `-d` | Run container in detached mode (background) |
| | `-it` | Interactive terminal (input/output attached) |
| | `-p <host>:<container>` | Map ports (host port to container port) |
| | `-e KEY=VALUE` | Set environment variables |
| | `--name <name>` | Assign a container name |
| | `-v <path>:<path>` | Mount volumes (bind mounts) |
| | `--rm` | Automatically remove container when it exits |
| `docker ps` | `-a` | List all containers (running and stopped) |
| | `-q` | Show only container IDs |
| `docker stop` | `<container>` | Stop a running container (graceful shutdown) |
| `docker start` | `<container>` | Start a stopped container |
| `docker restart` | `<container>` | Restart a container |
| `docker rm` | `-f` | Remove a container (force if running) |
| `docker logs` | `-f` | Stream container logs in real-time |
| | `--tail <n>` | Show only last N lines of logs |
| `docker exec` | `-it` | Execute a command inside a running container |
| `docker inspect` | N/A | View detailed information about a container/image |

#### System Commands
| Command | Flags | Description |
|---------|-------|-------------|
| `docker system prune` | `-a` | Remove unused containers, images, networks, and volumes |
| | `--volumes` | Also remove unused volumes |
| `docker volume ls` | N/A | List all volumes |
| `docker volume rm` | `<volume>` | Remove a volume |
| `docker network ls` | N/A | List all networks |

### Docker Compose Commands

| Command | Flags | Description |
|---------|-------|-------------|
| `docker compose up` | `-d` | Create and start all services in detached mode |
| | `--build` | Build images before starting services |
| | `-f <file>` | Use a specific docker-compose file |
| `docker compose down` | `--volumes` | Stop and remove containers (and volumes if flag used) |
| | `--rmi all` | Remove all images |
| `docker compose ps` | N/A | List all services and their status |
| `docker compose logs` | `-f` | View and follow logs from all services |
| | `<service>` | View logs for a specific service only |
| `docker compose exec` | `<service> <command>` | Execute a command in a running service |
| `docker compose build` | `--no-cache` | Build images without cache |
| `docker compose restart` | `<service>` | Restart a service (omit service name to restart all) |
| `docker compose stop` | `<service>` | Stop a service |
| `docker compose start` | `<service>` | Start a stopped service |
| `docker compose rm` | `-f` | Remove stopped containers |

### Common Usage Examples

**Start a Python application with a PostgreSQL database:**
```bash
docker compose up -d
```

**Check the status of all services:**
```bash
docker compose ps
```

**View logs from the web service in real-time:**
```bash
docker compose logs -f web
```

**Execute a command in the database service:**
```bash
docker compose exec db psql -U myuser -d mydb
```

**Rebuild all images and start services:**
```bash
docker compose up --build -d
```

**Stop and remove all containers, networks, and volumes:**
```bash
docker compose down --volumes
```

**Run a standalone container with a bash shell:**
```bash
docker run -it ubuntu /bin/bash
```

**Build an image from a Dockerfile:**
```bash
docker build -t myapp:1.0 .
```

**Clean up unused Docker resources:**
```bash
docker system prune -a --volumes
```
