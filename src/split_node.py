from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    if not old_nodes or not isinstance(old_nodes,list) or not all(isinstance(node, TextNode) for node in old_nodes):
        raise ValueError("Old_nodes must be a populated list of TextNode objects")
    

    new_nodes = []
    
    match delimiter:
        case "**":
            split_type = 'bold'
        case "*":
            split_type = 'itallic'
        case "`":
            split_type = 'code'
        case _:
            raise ValueError("Invalid delimiter type. Must use: **, *, or `")
        
    for node in old_nodes:

        if node.text_type != 'text':
            new_nodes.append(node)
        
        sections = node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown syntax, missing opening or closing delimiter")
        
        for i in range(len(sections)):
            if i % 2 == 0:
                if not sections[i]:
                    continue
                new_nodes.append(TextNode(sections[i], 'text'))   
            else:
                new_nodes.append(TextNode(sections[i], split_type))
    return new_nodes