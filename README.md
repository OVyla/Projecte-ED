# Pràctica Estructures de Dades

Avui en dia existeixen moltes utilitats per a gestionar biblioteques de vídeos. Una característica apreciada pels usuaris és la capacitat de fer recomanacions basades en les seves preferències.
En aquesta pràctica s’implementarà un sistema senzill de reproducció i recomanació de vídeos.
Una característica important d’aquesta pràctica serà la utilització d’estructures de dades adients per a optimitzar tant l’ús de la memòria com l’execució de les operacions del gestor de la col·lecció de vídeos.

Aquesta pràctica es pot catalogar dintre del conjunt d’aplicatius anomenats Gestors de Vídeos o Video Managers. Aquestes aplicacions tenen com a objectiu principal emmagatzemar i gestionar les col·leccions de vídeos dels usuaris, proporcionant determinades funcionalitats auxiliars com ara la creació de llistes de reproducció i recomanacions de seqüències de vídeos. Òbviament, la pràctica no consisteix en construir una aplicació comercial d’aquest tipus. Però sí que s’implementaran algunes de les funcionalitats típiques d’aquestes aplicacions, entre elles:
- Recuperació de metadades (títol, data, gènere, etc.) d’arxius mp4.
- Gestió de llistes de reproducció M3U dels vídeos d’una determinada col·lecció.
- Reproducció dels vídeos en format mp4.
- Recomanacions basades en cerques i creuament de metadades.
Dintre d’aquest domini la pràctica desenvolupada haurà de realitzar amb la suficient eficiència les tasques que s’aniran descrivint. Mostrant així la utilitat de fer servir estructures de dades complexes per augmentar el rendiment del processament de dades. A més, no només el rendiment haurà de ser suficientment bo, sinó que la implementació a baix nivell de les estructures de dades haurà de ser correcta i robusta. Això es comprovarà realitzant una sèrie de tests que avaluaran l’execució —incloent casos extrems— dintre d’un corpus de vídeos donat (a banda de l’òbvia depuració i les proves que vosaltres ja heu de fer habitualment durant el desenvolupament).
