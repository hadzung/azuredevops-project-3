resource "azurerm_network_interface" "my_nic" {
  name                = "MyNICforProj3"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_id
  }
}

resource "azurerm_linux_virtual_machine" "myAgent" {
  name                = "project3-myAgent"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS2_v2"
  admin_username      = "myAdmin"
  network_interface_ids = [azurerm_network_interface.my_nic.id]
  admin_ssh_key {
    username   = "myAdmin"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCjc6dnP0XTUzCymkWLQswB8K3x7883uUxv4FzuX5nU0dqOPdzCe/Vnk2FRnVCVGw+FM/xhLl/p49qVzxarBjKp0Ug2pME4yqPANTGzkVuAf10KmDcXlxK9MCdSbh6LvG1p9QnTB4pMYcPVO2Na4s7Ot3gis4RHgOyUg92fJxT5SuVPKUW/y3VwtrMAlQye2xCHbsIxup8e5NvFvNnQ9HAoRLMKiOuDNmxUSW1VZ3MBTUnm03YbfxOWbMPOZuXjSJrsfYCo1ZPraz8j11FmZFEbO8zMKaGdsYUdFQ+/DXFBbOUnWs2p9FYMwD2MZFRqObCirvKD0uIRqS/TBzIXeeRa4/lwqkKfgWsS84vUemdTbY7pjP2rSeK4qIAPttSbzL+vmsmV/4NNoFWIFRJ/GR7xRjy+zU90VlM6+GqP9+ERyx7ebXlBCBuYs9sh22bC751R0DPa6b7R+GIFq3KmPpW97g94j7WbvNFfpJIiRUh1lQJMar8BUqttI71UfDFKGYE= dzungha@DESKTOP-A57PFHD"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}

resource "azurerm_linux_virtual_machine" "test_env" {
  name                = "project3-test-env"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS2_v2"
  admin_username      = "myAdmin"
  network_interface_ids = [azurerm_network_interface.my_nic.id]
  admin_ssh_key {
    username   = "myAdmin"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCjc6dnP0XTUzCymkWLQswB8K3x7883uUxv4FzuX5nU0dqOPdzCe/Vnk2FRnVCVGw+FM/xhLl/p49qVzxarBjKp0Ug2pME4yqPANTGzkVuAf10KmDcXlxK9MCdSbh6LvG1p9QnTB4pMYcPVO2Na4s7Ot3gis4RHgOyUg92fJxT5SuVPKUW/y3VwtrMAlQye2xCHbsIxup8e5NvFvNnQ9HAoRLMKiOuDNmxUSW1VZ3MBTUnm03YbfxOWbMPOZuXjSJrsfYCo1ZPraz8j11FmZFEbO8zMKaGdsYUdFQ+/DXFBbOUnWs2p9FYMwD2MZFRqObCirvKD0uIRqS/TBzIXeeRa4/lwqkKfgWsS84vUemdTbY7pjP2rSeK4qIAPttSbzL+vmsmV/4NNoFWIFRJ/GR7xRjy+zU90VlM6+GqP9+ERyx7ebXlBCBuYs9sh22bC751R0DPa6b7R+GIFq3KmPpW97g94j7WbvNFfpJIiRUh1lQJMar8BUqttI71UfDFKGYE= dzungha@DESKTOP-A57PFHD"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}