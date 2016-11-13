# NginxConfig
Create NGINX config files from Python dicts.

# Usage
```
config = NginxConfig('/etc/nginx/sites-available/test.conf')
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

This is just a class that I thought might be handy for some particular usage scenarios - that's all.
