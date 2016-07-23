from django import forms

from . import models

class NodeConfigForm(forms.ModelForm):
    class Meta:
        model = models.NodeConfig
        fields = ['node_id',
                 'node_configuration',]
                 #'log_time']
        #widgets = {'nodes': CheckboxSelectMultiple}
        labels = {
                'node_id': 'Choose node',
                'node_configuration': 'Enter Configuration'
        }
        '''
        help_texts = {
           'node_configuration': 'Enter here configuration!',
       }
       '''
