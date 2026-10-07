# Task 13 - Delivery Promise Calculator
# Configuration management using Puppet

$delivery_root = 'C:/DeliveryPromise'

file { $delivery_root:
  ensure => directory,
}

file { "${delivery_root}/config":
  ensure  => directory,
  require => File[$delivery_root],
}

file { "${delivery_root}/logs":
  ensure  => directory,
  require => File[$delivery_root],
}

file { "${delivery_root}/config/application.properties":
  ensure  => file,
  content => @("PROPERTIES"),
spring.application.name=delivery-promise-calculator
server.port=8765
| PROPERTIES
  require => File["${delivery_root}/config"],
}