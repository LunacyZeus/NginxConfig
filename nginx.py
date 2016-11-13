class NginxConfig:
    NODE_TEMPLATE = '{0}{1} {2};\n'
    NODE_GROUP_TEMPLATE = '\n{0}{1} {{\n\n{2}\n{0}}}\n\n'

    WHITESPACE = ' '

    def __init__(self, config_file, read_only=True):
        if not read_only:
            self.config_file = open(config_file, 'w+')
        else:
            self.config_file = open(config_file, 'r')

        self.output = ''

    def make(self, key, item, indent=0, nested=False):
        output = ''
        try:
            if nested:
                indent = indent + 4

            output_nested = ''
            for nested_key, nested_item in item.iteritems():
                output_nested = output_nested + self.make(nested_key, nested_item, indent, nested=True)

            output = output + self.NODE_GROUP_TEMPLATE.format(self.WHITESPACE * indent, key, output_nested)
        except AttributeError:
            output = output + self.NODE_TEMPLATE.format(self.WHITESPACE * indent, key, item)

        return output

    def build(self, raw):
        for key, item in raw.iteritems():
            self.output = self.output + self.make(key, item)

    def save(self):
        output = '# Generated with NginxConfig by Jordan Brown (www.bytestack.io)\n\n' + self.output
        self.config_file.write(output)
