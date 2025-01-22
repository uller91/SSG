class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
        
    def props_to_html(self):
        if self.props is None:
            return ""
        
        props_line = ""
        for key, value in self.props.items():
            props_line += f' {key}="{value}"'
            #print(props_line)
        return props_line
        


    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"