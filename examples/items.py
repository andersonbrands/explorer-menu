from explorermenu.menu_items import node
from explorermenu import cmd

single_action_item = node('Root action', cmd('echo Root action', keep_cmd_window=True))

nested_set = \
    node('Root',
         node('Child 1',
              node('Grand child 1',
                   node('Grandgrand child 1', cmd('echo Grandgrand child 1 action', keep_cmd_window=True)),
                   node('Grandgrand child 2', cmd('echo Grandgrand child 2 action', keep_cmd_window=True)),
                   ),
              node('Grand child 2', cmd('echo Grand child 2 action', keep_cmd_window=True))
              ),
         node('Child 2', cmd('echo Child 2 action', keep_cmd_window=True)),
         )
