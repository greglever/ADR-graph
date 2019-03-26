Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y python3-pip  # apt-get install r-base-core  pip install rpy2==2.7.4
  SHELL
end

