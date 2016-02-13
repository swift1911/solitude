from fabric.api import (
    task,
    env,
    execute,
    hosts,
    sudo,
)

#fab task
@task
@hosts(['prod-1'])
def deploy():
    sudo("mkdir -p /data/solitude")



#refrash service
def python_refresh():
    sudo("supervisorctl update")
    sudo("supervisorctl quickrestart")
