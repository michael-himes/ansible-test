if ENV['SUB_USERNAME' && 'SUB_PASSWORD'].nil? 
  puts "Please set the following:"
  puts "export SUB_USERNAME=\nexport SUB_PASSWORD="
  exit 1 
else
  username, password = ENV['SUB_USERNAME'], ENV['SUB_PASSWORD'] 
end

if Dir.glob("*.gz").any?
  tar_file = Dir.glob("ansible*.tar.gz")[0] 
  tar_dir = File.basename("#{tar_file}", ".tar.gz") 
end

Vagrant.configure("2") do |config|
  config.registration.username = "#{username}"
  config.registration.password = "#{password}"
  config.registration.unregister_on_halt = false
  config.vm.define :tower do |tower|
    tower.vm.hostname = "tower"
    tower.vm.box = "generic/rhel8"
    tower.vm.network :private_network, ip: "172.16.0.101"
    if defined?(tar_file)
      tower.vm.provision "ansible" do |all|
        all.verbose = "v"
        all.playbook = "install_tower.yml"
        all.limit = "all"
        all.extra_vars = {
          "ansible_tower_tar": "#{tar_file}",
          "ansible_tower_directory": "#{tar_dir}",
          "redhat_subscription_username": "#{username}",
          "redhat_subscription_password": "#{password}"
        }
        all.groups = {
          "tower" => ["tower"],
          "database" => ["db"],
          "automationhub" => ["auto"],
          "test" => ["test"]
        }
      end
      tower.vm.provision "shell", inline: "cd #{tar_dir}; sudo ./setup.sh -e ignore_preflight_errors=True"
    end
    tower.vm.provider :libvirt do |libvirt|
      libvirt.memory = 2048
      libvirt.cpus = 2
    end
  end

  config.vm.define :db do |db|
    db.vm.hostname = "db"
    db.vm.box = "generic/rhel8"
    db.vm.network :private_network, ip: "172.16.0.102"
    db.vm.provider :libvirt do |libvirt|
      libvirt.memory = 2048
      libvirt.cpus = 2
    end
  end

  config.vm.define :auto do |auto|
    auto.vm.hostname = "auto"
    auto.vm.box = "generic/rhel8"
    auto.vm.network :private_network, ip: "172.16.0.103"
    auto.vm.provider :libvirt do |libvirt|
      libvirt.memory = 2048
      libvirt.cpus = 2
    end
  end

  config.vm.define :test do |test|
    test.vm.hostname = "test"
    test.vm.box = "generic/rhel8"
    test.vm.network :private_network, ip: "172.16.0.104"
    test.vm.provider :libvirt do |libvirt|
      libvirt.memory = 2048
      libvirt.cpus = 2
    end
  end
end
