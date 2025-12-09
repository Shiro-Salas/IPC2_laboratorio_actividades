import xml.etree.ElementTree as ET

def main():
    print("\n" + "=" * 50)
    print("Reporte de envíos -- TransExpress --")
    print("=" * 50)

    try:
        #bloque de codigo donde se carga el archivo envios.xml
        tree = ET.parse('envios.xml')
        root = tree.getroot()

        #bloque de codigo para mostrar la información del nodo raiz
        print(f"\nNodo raíz: {root.tag}")
        print(f"Fecha de reporte: {root.get('fecha')}")
        print("-" * 30)

        #bloque de código para recorree cada registro de envio, obtener y mostrar la informacion recopilada
        for envio in root.findall('envio'):

            envio_id = envio.get('id')
            nombre_cliente = envio.find('cliente/nombre').text #manejo por rutas 
            telefono_cliente = envio.find('cliente/telefono').text
            paquete = envio.find('paquete')
            descripcion = paquete.find('description').text #manejo escalonado (puedo trabajarlo con los dos, es cuestion de gusto)
            peso = paquete.get('peso')
            unidad = paquete.get('unidad')
            estado = envio.find('estado').text

            print(f"\nID  del envío: {envio_id}")
            print(f"Cliente: {nombre_cliente}")
            print(f"Teléfono: {telefono_cliente}")
            print(f"Paquete: {descripcion}")
            print(f"peso: {peso} {unidad}")
            print(f"Estado: {estado}")
        
        print("\n" + "-" *30)
        print("\nReporte generado exitosamente")
        print(f"Total de envíos: {len(root.findall('envio'))}")

    except FileNotFoundError:
        print("El archivo 'envios.xml' no se encontró.")
    except ET.ParseError:
        print("El archivo 'envios.xml' tiene formato incorrecto.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
            