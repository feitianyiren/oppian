class oppian {

  $project = "oppianproj"
  $debug_django = "True"

  class { "webapp::python": owner => "root",
                          group => "wheel",
                          src_root => "/deploy",
                          nginx_workers => 1,
                          monit_admin => "matt@oppian.com",
                          monit_interval => 30,
  }

  webapp::python::instance { $project:
    workers => inline_template("<%= (processorcount.to_i * 2 + 1) -%>"),
    listen_port => 8080,
    domain => "oppian.com",
    django => true,
    requirements => true,
    django_syncdb => true,
    pythonpath => ["lib/django", "apps", "apps/oppianapp/utils", "lib/django-storages"],
  }

  file { "/deploy/$project/settings_local.py":
    ensure => file,
    content => template('oppian/settings.py.erb'),
  }

  class {'varnish':}

}
