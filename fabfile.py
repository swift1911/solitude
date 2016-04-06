from fabric.api import (
    task,
    env,
    execute,
    hosts,
    sudo,
    local,
    cd
)

host = 'sg-linode'


# fab task
@task
@hosts([host])
def deploy():
    remote_dir = '/data/solitude'
    local_dir = '.'
    sudo("mkdir -p {0}".format(remote_dir))
    local("rsync -azq --progress --force --delete --delay-updates "
          "{0} {1}:{2}/ ".format(
        local_dir,
        host,
        remote_dir,
    ))
    with cd(remote_dir):
        sudo('pip install -r requirements.txt')
        sudo('cp solitude.ini /etc/supervisord.d/')
        sudo('mkdir -p /data/log/solitude')
        sudo('supervisorctl update')
        sudo('supervisorctl restart solitude')

# refrash service
def python_refresh():
    sudo("supervisorctl update")
    sudo("supervisorctl quickrestart")
