if Dir.glob("*.gz")
  TAR_FILE = Dir.glob("*.gz")[0] 
  TAR = File.basename("#{TAR_FILE}", ".tar.gz") 
end


$script = <<-SCRIPT

tar xf #{TAR_FILE} 
mv -f inventory #{TAR}

SCRIPT


Vagrant.configure("2") do |config|

  config.vm.define :tower do |tower|
    tower.vm.box = "generic/rhel8"
    tower.vm.network :private_network, ip: "10.0.15.101"
    tower.vm.provision "file", :source => "#{TAR_FILE}", :destination => "/home/vagrant/"
    if File.exist?("inventory")
      tower.vm.provision "file", :source => "inventory", :destination => "/home/vagrant/"
    end
    tower.vm.provision "shell", inline: $script
    tower.vm.provider :libvirt do |libvirt|
      libvirt.memory = 2048
      libvirt.cpus = 2
    end
  end

  config.vm.define :db do |db|
    db.vm.box = "generic/rhel8"
    db.vm.network :private_network, ip: "10.0.15.102"
    db.vm.provider :libvirt do |libvirt|
      libvirt.memory = 2048
      libvirt.cpus = 2
    end
  end

  config.vm.define :auto do |auto|
    auto.vm.box = "generic/rhel8"
    auto.vm.network :private_network, ip: "10.0.15.103"
    auto.vm.provider :libvirt do |libvirt|
      libvirt.memory = 2048
      libvirt.cpus = 2
    end
  end

  config.vm.define :test do |test|
    test.vm.box = "generic/rhel8"
    test.vm.network :private_network, ip: "10.0.15.104"
    test.vm.provider :libvirt do |libvirt|
      libvirt.memory = 2048
      libvirt.cpus = 2
    end
  end

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
  end
end
