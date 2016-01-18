##Despliegue directo desde el repositorio de Github :SnapCI

Finalmente configuramos el despliegue directo desde el repositorio de Github y la herramienta Snap CI para realizar el despliegue simplemente haciendo push desde el repositorio

***Con Snap CI***

La configuración es tan fácil como añadir nuestro repositorio de github a snap CI.

![http://i1175.photobucket.com/albums/r624/Bob_Mures/editmeSnapCi_zpspjwzj8t3.png](http://i1175.photobucket.com/albums/r624/Bob_Mures/editmeSnapCi_zpspjwzj8t3.png)
Figura en la que se se muestra los comandos para instalar las dependencias.

![http://i1175.photobucket.com/albums/r624/Bob_Mures/deploySnapCI_zpspxbchdgb.png](http://i1175.photobucket.com/albums/r624/Bob_Mures/deploySnapCI_zpspxbchdgb.png)

Figura en la que se configura la configuración

![http://i1175.photobucket.com/albums/r624/Bob_Mures/snapCI_zpsldwylygu.png](http://i1175.photobucket.com/albums/r624/Bob_Mures/snapCI_zpsldwylygu.png)

Y ya tenemos la integración contínua que despliega la aplicación al hacer git push a nuestro repositorio de GitHub, siempre que esta pase los tests.

