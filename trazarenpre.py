#!/usr/bin/python
# -*- coding: latin-1 -*-
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

"M�dulo para Trazabilidad de Precursores Qu�micos RENPRE Resoluci�n 900/12"

# Informaci�n adicional y documentaci�n:
# http://www.sistemasagiles.com.ar/trac/wiki/TrazabilidadPrecursoresQuimicos

__author__ = "Mariano Reingart <reingart@gmail.com>"
__copyright__ = "Copyright (C) 2011 Mariano Reingart"
__license__ = "GPL 3.0+"
__version__ = "1.10a"

#http://renpre.servicios.pami.org.ar/portal_traza_renpre/paso5.html

import os
import socket
import sys
import datetime, time
import pysimplesoap.client
from pysimplesoap.client import SoapFault
from utils import BaseWS, inicializar_y_capturar_excepciones, get_install_dir

HOMO = False
TYPELIB = False

WSDL = "https://trazabilidad.pami.org.ar:59050/trazamed.WebServiceSDRN?wsdl"
LOCATION = "https://trazabilidad.pami.org.ar:59050/trazamed.WebServiceSDRN?wsdl"
         

class TrazaRenpre(BaseWS):
    "Interfaz para el WebService de Trazabilidad de Medicamentos ANMAT - PAMI - INSSJP"
    _public_methods_ = ['SaveTransacciones',
                        'SendCancelacTransacc',
                        'Conectar', 'LeerError', 'LeerTransaccion',
                        'SetUsername', 
                        'SetParametro', 'GetParametro',
                        'GetCodigoTransaccion', 'GetResultado', 'LoadTestXML']
                        
    _public_attrs_ = [
        'Username', 'Password', 
        'CodigoTransaccion', 'Errores', 'Resultado',
        'XmlRequest', 'XmlResponse', 
        'Version', 'InstallDir', 
        'Traceback', 'Excepcion',
        ]

    _reg_progid_ = "TrazaRenpre"
    _reg_clsid_ = "{461298DB-0531-47CA-B3D9-B36FE6967209}"

    # Variables globales para BaseWS:
    HOMO = HOMO
    WSDL = WSDL
    Version = "%s %s %s" % (__version__, HOMO and 'Homologaci�n' or '', 
                            pysimplesoap.client.__version__)

    def __init__(self, reintentos=1):
        self.Username = self.Password = None
        BaseWS.__init__(self, reintentos)

    def inicializar(self):
        BaseWS.inicializar(self)
        self.CodigoTransaccion = self.Errores = self.Resultado = None

    def __analizar_errores(self, ret):
        "Comprueba y extrae errores si existen en la respuesta XML"
        self.Errores = ["%s: %s" % (it['_c_error'], it['_d_error'])
                        for it in ret.get('errores', [])]
        self.Resultado = ret.get('resultado')

    def Conectar(self, cache=None, wsdl=None, proxy="", wrapper=None, cacert=None, timeout=None):
        # Conecto usando el m�todo estandard:
        ok = BaseWS.Conectar(self, cache, wsdl, proxy, wrapper, cacert, timeout, 
                             soap_server="jetty")
        if ok:
            # Establecer credenciales de seguridad:
            self.client['wsse:Security'] = {
                'wsse:UsernameToken': {
                    'wsse:Username': self.Username,
                    'wsse:Password': self.Password,
                    }
                }
        return ok
        
    @inicializar_y_capturar_excepciones
    def SaveTransacciones(self, usuario, password, 
                         gln_origen=None, gln_destino=None, f_operacion=None, 
                         id_evento=None, cod_producto=None, n_cantidad=None, 
                         n_documento_operacion=None, n_remito=None, 
                         id_tipo_transporte=None, 
                         id_paso_frontera_ingreso=None, 
                         id_paso_frontera_egreso=None, 
                         id_tipo_documento_operacion=None, 
                         d_dominio_tractor=None, 
                         d_dominio_semi=None, 
                         n_serie=None, n_lote=None, doc_despacho_plaza=None, 
                         djai=None, n_cert_rnpq=None, 
                         id_tipo_documento=None, n_documento=None, 
                         m_calidad_analitica=None
                         ):
        "Permite informe por parte de un agente de una o varias transacciones"
        # creo los par�metros para esta llamada
        params = {  'gln_origen': gln_origen, 'gln_destino': gln_destino,
                    'f_operacion': f_operacion, 'id_evento': id_evento,
                    'cod_producto': cod_producto, 'n_cantidad': n_cantidad, 
                    'n_documento_operacion': n_documento_operacion, 
                    'n_remito': n_remito, 
                    'id_tipo_transporte': id_tipo_transporte, 
                    'id_paso_frontera_ingreso': id_paso_frontera_ingreso, 
                    'id_paso_frontera_egreso': id_paso_frontera_egreso, 
                    'id_tipo_documento_operacion': id_tipo_documento_operacion, 
                    'd_dominio_tractor': d_dominio_tractor, 
                    'd_dominio_semi': d_dominio_semi, 
                    'n_serie': n_serie, 'n_lote': n_lote, 
                    'doc_despacho_plaza': doc_despacho_plaza, 
                    'djai': djai, 'n_cert_rnpq': n_cert_rnpq, 
                    'id_tipo_documento': id_tipo_documento, 
                    'n_documento': n_documento, 
                    'm_calidad_analitica': m_calidad_analitica,
                    }
        # actualizo con par�metros generales:
        params.update(self.params_in)
        res = self.client.saveTransacciones(
            arg0=params,
            arg1=usuario, 
            arg2=password,
        )
        ret = res['return']        
        self.CodigoTransaccion = ret['codigoTransaccion']
        self.__analizar_errores(ret)
        return True

    @inicializar_y_capturar_excepciones
    def SendCancelacTransacc(self, usuario, password, codigo_transaccion):
        " Realiza la cancelaci�n de una transacci�n"
        res = self.client.sendCancelaTransac(
            arg0=codigo_transaccion, 
            arg1=usuario, 
            arg2=password,
        )

        ret = res['return']
        
        self.CodigoTransaccion = ret['codigoTransaccion']
        self.__analizar_errores(ret)

        return True

    @inicializar_y_capturar_excepciones
    def SendConfirmaTransacc(self, usuario, password, p_ids_transac, f_operacion):
        "Confirma la recepci�n de un medicamento"
        res = self.client.sendConfirmaTransacc(
            arg0=usuario, 
            arg1=password,
            arg2={'p_ids_transac': p_ids_transac, 'f_operacion': f_operacion}, 
        )
        ret = res['return']
        self.CodigoTransaccion = ret.get('id_transac_asociada')
        self.__analizar_errores(ret)
        return True

    @inicializar_y_capturar_excepciones
    def SendAlertaTransacc(self, usuario, password, p_ids_transac_ws):
        "Alerta un medicamento, acci�n contraria a �confirmar la transacci�n�."
        res = self.client.sendAlertaTransacc(
            arg0=usuario, 
            arg1=password,
            arg2=p_ids_transac_ws, 
        )
        ret = res['return']
        self.CodigoTransaccion = ret.get('id_transac_asociada')
        self.__analizar_errores(ret)
        return True

    def SetUsername(self, username):
        "Establezco el nombre de usuario"        
        self.Username = username

    def SetPassword(self, password):
        "Establezco la contrase�a"        
        self.Password = password

    def GetCodigoTransaccion(self):
        "Devuelvo el c�digo de transacci�n"        
        return self.CodigoTransaccion

    def GetResultado(self):
        "Devuelvo el resultado"        
        return self.Resultado



def main():
    "Funci�n principal de pruebas (transaccionar!)"
    import os, time, sys
    global WSDL, LOCATION

    DEBUG = '--debug' in sys.argv

    ws = TrazaRenpre()
    
    ws.Username = 'testwservice'
    ws.Password = 'testwservicepsw'
    
    if '--prod' in sys.argv and not HOMO:
        WSDL = "https://servicios.pami.org.ar/trazarenpre.WebServiceSDRN"
        print "Usando WSDL:", WSDL
        sys.argv.pop(0)
    
    ws.Conectar("", WSDL)
    
    if ws.Excepcion:
        print ws.Excepcion
        print ws.Traceback
        sys.exit(-1)
    
    #print ws.client.services
    #op = ws.client.get_operation("sendMedicamentos")
    #import pdb;pdb.set_trace()
    if '--test' in sys.argv:
        ws.SaveTransacciones(
            usuario='pruebasws', password='pruebasws',
            gln_origen=8888888888888,
            gln_destino=4,
            f_operacion="01/01/2012",
            id_evento=40,
            cod_producto=12312312313255,
            n_cantidad=1,
            n_documento_operacion=1,
            #m_entrega_parcial="",
            n_remito=123,
            n_serie=112,
            )
        print "Resultado", ws.Resultado
        print "CodigoTransaccion", ws.CodigoTransaccion
        print "Excepciones", ws.Excepcion
        print "Erroes", ws.Errores
    elif '--cancela' in sys.argv:
        ws.SendCancelacTransacc(*sys.argv[sys.argv.index("--cancela")+1:])
    else:
        ws.SaveTransacciones(*sys.argv[1:])
    print "|Resultado %5s|CodigoTransaccion %10s|Errores|%s|" % (
            ws.Resultado,
            ws.CodigoTransaccion,
            '|'.join(ws.Errores),
            )
    if ws.Excepcion:
        print ws.Traceback

# busco el directorio de instalaci�n (global para que no cambie si usan otra dll)
INSTALL_DIR = TrazaRenpre.InstallDir = get_install_dir()


if __name__ == '__main__':

    # ajusto el encoding por defecto (si se redirije la salida)
    if sys.stdout.encoding is None:
        import codecs, locale
        sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout,"replace");
        sys.stderr = codecs.getwriter(locale.getpreferredencoding())(sys.stderr,"replace");

    if '--register' in sys.argv or '--unregister' in sys.argv:
        import pythoncom
        import win32com.server.register
        win32com.server.register.UseCommandLine(TrazaRenpre)
    elif "/Automate" in sys.argv:
        # MS seems to like /automate to run the class factories.
        import win32com.server.localserver
        #win32com.server.localserver.main()
        # start the server.
        win32com.server.localserver.serve([TrazaRenpre._reg_clsid_])
    else:
        main()
