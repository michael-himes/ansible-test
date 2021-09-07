def redhat_subscription_auth
  puts "Redhat Subscription Username:"
  username = STDIN.gets.chomp
  puts "Redhat Subscription Password:"
  password = STDIN.noecho(&:gets).chomp
  return [ username, password ]
end

if ENV['SUB_USERNAME' && 'SUB_PASSWORD'].nil? 
  puts "Please consider setting environment variables SUB_USERNAME' and 'SUB_PASSWORD' to avoid multiple credentail prompts.\n Example: \n\t export SUB_USERNAME=username \n\t export SUB_PASSWORD=password \n"
  username, password = redhat_subscription_auth()
else 
  username = ENV['SUB_USERNAME']
  password = ENV['SUB_PASSWORD']
end

if Dir.glob("*.gz").any?
  tar_file = Dir.glob("*.gz")[0] 
  tar_dir = File.basename("#{tar_file}", ".tar.gz") 
  task_file = "/home/vagrant/#{tar_dir}/roles/preflight/tasks/main.yml"
end


Vagrant.configure("2") do |config|

  config.vm.define :tower do |tower|
    tower.vm.box = "generic/rhel8"
    tower.vm.network :private_network, ip: "10.0.15.101"
    if defined?(tar_file)
      tower.vm.provision "file", :source => "#{tar_file}", :destination => "/home/vagrant/"
      tower.vm.provision "ansible" do |ansible|
        ansible.verbose = "vvvv"
        ansible.playbook = "tower.yml"
        ansible.extra_vars = {
          "redhat_subscription_username": "#{username}",
          "redhat_subscription_password": "#{password}"
        }
      end
      if File.exist?("inventory")
        tower.vm.provision "file", :source => "inventory", :destination => "/home/vagrant/"
        tower.vm.provision "shell", inline: "mv -f inventory #{tar_dir}"
      end
      #tower.vm.provision "shell", inline: "cd #{tar_dir}; sudo ./setup.sh -- --skip-tags 'ram'"
    end

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
    auto.vm.provision "ansible" do |ansible|
      ansible.verbose = "v"
      ansible.playbook = "auto.yml"
      ansible.extra_vars = {
        "redhat_subscription_username": "#{username}",
        "redhat_subscription_password": "#{password}"
      }
    end

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

  config.vm.provision "ansible" do |all|
    all.verbose = "v"
    all.playbook = "all.yml"
    all.extra_vars = {
      "redhat_subscription_username": "#{username}",
      "redhat_subscription_password": "#{password}"
    }
  end
end
