# NginxConfig
Create NGINX config files from Python dicts.

# Usage
```
config = Config('/etc/nginx/sites-available/test.conf')
config.build({
  'group': {
    'key1': 'val1',
    'key2': 'val2',
    'group2': {
      'key3': 'val3'
    }
  }
})
config.save()
```
...would generate...
```
group {
    key val1;
    key val2;
    
    group2 {
        key3 val3;
    }
}
```
