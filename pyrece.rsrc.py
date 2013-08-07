{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':u'Aplicativo Factura Electr\xf3nica (PyRece)',
          'size':(592, 265),

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuArchivo',
             'label':u'Archivo',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuArchivoAbrir',
                   'label':u'Abrir',
                  },
                  {'type':'MenuItem',
                   'name':'menuArchivoCargar',
                   'label':u'ReCargar',
                  },
                  {'type':'MenuItem',
                   'name':'menuArchivoGuardar',
                   'label':u'Guardar',
                  },
##                  {'type':'MenuItem',
##                   'name':'menuArchivoDiseniador',
##                   'label':u'Dise�ador',
##                  },
              ]
             },
             {'type':'Menu',
             'name':'menuConsultas',
             'label':u'Consultas',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuConsultasDummy',
                   'label':u'Estado Servidores (Dummy)',
                  },
                  {'type':'MenuItem',
                   'name':'menuConsultasLastCBTE',
                   'label':u'\xdalt. Cbte.',
                  },
                  {'type':'MenuItem',
                   'name':'menuConsultasLastID',
                   'label':u'\xdalt. ID',
                  },
                  {'type':'MenuItem',
                   'name':'menuConsultasGetCAE',
                   'label':u'Recuperar CAE',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuAyuda',
             'label':u'Ayuda',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuAyudaInstructivo',
                   'label':u'Instructivo',
                  },
                  {'type':'MenuItem',
                   'name':'menuAyudaAcercaDe',
                   'label':u'Acerca de',
                  },
                  {'type':'MenuItem',
                   'name':'menuAyudaLimpiar',
                   'label':u'Limpiar estado',
                  },
                  {'type':'MenuItem',
                   'name':'menuAyudaMensajesXML',
                   'label':u'Mensajes XML',
                  },
                  {'type':'MenuItem',
                   'name':'menuAyudaVerEstado',
                   'label':u'Ver/Ocultar Estado',
                  },
                  {'type':'MenuItem',
                   'name':'menuAyudaVerConfiguracion',
                   'label':u'Ver Configuraci�n',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'lblWebservice', 
    'position':(18, 10), 
    'text':u'Webservice:', 
    },

{'type':'Choice', 
    'name':'cboWebservice', 
    'position':(102, 5), 
    'size':(89, -1), 
    'items':[u'wsfe', u'wsfev1', u'wsfexv1'], 
    },


{'type':'Button', 
    'name':'btnMarcarTodo', 
    'position':(297, 163), 
    'label':u'Marcar Todo', 
    'toolTip':u'Seleccionar todas las facturas', 
    },

{'type':'Button', 
    'name':'btnAutorizarLote', 
    'position':(188, 163), 
    'label':u'Autorizar Lote', 
    'toolTip':u'Obtener CAE para todas las facturas', 
    },

{'type':'Button', 
    'name':'btnPrevisualizar', 
    'position':(395, 163), 
    'label':u'Previsualizar', 
    },


{'type':'Button', 
    'name':'btnAutenticar', 
    'position':(20, 163), 
    'label':u'Autenticar', 
    'toolTip':u'Iniciar Sesin en la AFIP', 
    },

{'type':'TextArea', 
    'name':'txtEstado', 
    'position':(20, 243), 
    'size':(534, 212), 
    'font':{'faceName': u'Sans', 'family': 'sansSerif', 'size': 8}, 
    'text':u'\n', 
    },

{'type':'StaticText', 
    'name':'lblProgreso', 
    'position':(20, 194), 
    'text':u'Progreso:', 
    },

{'type':'StaticText', 
    'name':'lblEstado', 
    'position':(22, 219), 
    'text':u'Estado:', 
    },

{'type':'Button', 
    'name':'btnEnviar', 
    'position':(490, 163), 
    'size':(60, -1), 
    'label':u'Enviar', 
    'toolTip':u'Generar y enviar mails', 
    },

{'type':'TextField', 
    'name':'txtArchivo', 
    'position':(260, 5), 
    'size':(300, -1), 
    'text':u'facturas.csv', 
    'editable': False,
    },

{'type':'StaticText', 
    'name':'lblArchivo', 
    'position':(195, 10), 
    'text':u'Archivo:', 
    },


{'type':'Button', 
    'name':'btnAutorizar', 
    'position':(104, 163), 
    'label':u'Autorizar', 
    'toolTip':u'Obtener CAE por cada factura', 
    },

{'type':'MultiColumnList', 
    'name':'lvwListado', 
    'position':(18, 53), 
    'size':(537, 106), 
    'backgroundColor':(255, 255, 255, 255), 
    'columnHeadings':[], 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 8}, 
    'items':[], 
    'maxColumns':1000, 
    'rules':1, 
    },

{'type':'StaticText', 
    'name':'lblFacturas', 
    'position':(18, 35), 
    'size':(117, -1), 
    'text':u'Facturas:', 
    },

{'type':'Gauge', 
    'name':'pbProgreso', 
    'position':(89, 195), 
    'size':(477, 16), 
    'backgroundColor':(209, 194, 182, 255), 
    'layout':'horizontal', 
    'max':100, 
    'value':0, 
    },

] # end components
} # end background
] # end backgrounds
} }