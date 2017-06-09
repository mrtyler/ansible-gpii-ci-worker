import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_gitlab_service_enabled_and_running(Service):
    svc = Service("gitlab-runner")
    assert svc.is_enabled
    assert svc.is_running


def test_terraform_installed(Command):
    assert Command.exists("terraform")


def test_terragrunt_installed(Command):
    assert Command.exists("terragrunt")


def test_jq_installed(Command):
    assert Command.exists("jq")


def test_ssh_known_hosts_configured(File, Sudo):
    # Needed because .ssh is private (0700).
    with Sudo():
        ff = File("/home/gitlab-runner/.ssh/known_hosts")
        assert ff.contains("github.com")
