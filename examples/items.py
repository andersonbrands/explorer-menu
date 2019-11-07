import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from explorermenu.menu_items import node

single_action_item = node('Root action', 'cmd.exe /K echo Root action')

nested_set = \
    node('Root',
         node('Child 1',
              node('Grand child 1',
                   node('Grandgrand child 1', 'cmd.exe /K echo Grandgrand child 1 action'),
                   node('Grandgrand child 2', 'cmd.exe /K echo Grandgrand child 2 action'),
                   ),
              node('Grand child 2', 'cmd.exe /K echo Grand child 2 action')
              ),
         node('Child 2', 'cmd.exe /K echo Child 2 action'),
         )

