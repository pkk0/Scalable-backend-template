# Scalable backend template using FastAPI, PostgreSQL, SQLAlchemy, Alembic and Docker Swarm Mode

Create your backend easily using the latest technology.
<br>Pre-configured template consists of 3 main components:
1. API - build with:
- FastAPI - async, high-performance Python web framework 
- SQLAlchemy - async SQL toolkit and ORM
- Alembic - database migration tool
2. database - PostgreSQL  
3. database tool available from your browser - pgAdmin

Scalability is ensured thanks to Docker Swarm Mode.

You can also use API image and scale it with Kubernetes.
<br>However, Kubernetes it's not trivial, and it's not recommended for beginners.
## Configuration
The most important configuration sits in .env file.
<br>You should also take a look at docker-compose files.

## Local development
Open terminal and type <code>docker compose up</code>. It will start all services.

#### First usage

Run the above command, open another terminal and type:
<br><code>docker exec $(docker ps -f name=api -q | head -n 1) alembic upgrade head</code>
<br>It will run first migration and create sample database.

To make development smooth and use full power of your code editor, create a virtual python environment:
<br><code>python3 -m venv venv</code>

Now switch to it <code>. venv/bin/activate</code>

And install all needed packages <code>pip3 install -r requirements.txt</code>



Now you can play with your code freely!

<h2>Going to PRODUCTION</h2>
<h4>Preparations</h4>
To deploy backend, we will use Docker Swarm Mode - container orchestration system.

It means you need at least a single node cluster running.

Don't have one? Don't worry! 
<br>You can do it easily, even on your own computer with <code>docker swarm init</code>
<br>With that mode set on, you can easily add other servers to your cluster.

Next, on your manager node you have to build a docker image of API <code>docker build --tag api .</code>

Now, you have to make sure you configured your environmental variables in .env file!
<br>Load them on your manager node by typing <code>export $(cat .env)</code>

The last step is to make PostgreSQL data persistent.
<br>For that, you have to mark one of your nodes to always run PostgreSQL database.
<br>You can see all your nodes by running <code>docker node ls</code>
<br>Then you grab your chosen node ID and label it by typing
<br><code>docker node update --label-add postgres-data-node=true ID_OF_YOUR_CHOSEN_NODE</code>
<br>on your manager node.

#### Deploying backend
Simply run <code>docker stack deploy -c docker-compose-prod.yaml backend</code>

Yay! Your backend is working :) <b>Don't forget to make migrations!</b>

#### What next?
Now you can for example scale your API service with a command:
<br><code>docker service scale backend_api=10</code>
<br>You will have 10 similar services running behind load balancer. Simple!