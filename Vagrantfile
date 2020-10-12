Vagrant.configure("2") do |config|

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
  end

  config.vm.box = "ubuntu/bionic64"

  config.vm.define "elkstack" do |elkstack|
    # Network
    elkstack.vm.network "private_network", ip: "192.168.34.32"
    elkstack.vm.network "forwarded_port", guest: 80, host: 80, id: "nginx"
    # Sync Folders
    elkstack.vm.synced_folder './sfolder', '/sfolder'
    elkstack.vm.synced_folder "./vagrant", "/vagrant"
  end

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "provision.yml"
  end


end
