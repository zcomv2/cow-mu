import socket, random, time
#Bot vaca-mu para IRC version 2.3
 
botnick = b"Vaca-Mu"
amo= "Zcom"
server = b"irc.libera.chat"
puerto = 6667
canal = b"#parati"
socket_bot = socket.socket()
socket_bot.connect((server, puerto))
socket_bot.send(b"USER user usar usor :amateur\n")
socket_bot.send(b'NICK ' +botnick+b'\n')
 
 
def mu(num_option): 
  if num_option==0:  
      socket_bot.send(b"PRIVMSG "+ canal +b" :Las cosas no son como son, son como tu crees que son. hack 101\n")
  if num_option==1:  
      socket_bot.send(b"PRIVMSG "+ canal +b" :Mejor ir despacio y hacerlo bien, qie ir rapido y hacerlo mal.\n")
  if num_option==2:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Aveces es mejor parecer que no sabes nada, cuando en realidad lo sabes Todo.\n")
  if num_option==3:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Es importante hacer algunas donaciones a los Equipos del Open-Source\n")
  if num_option==4:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Debian The Universal Free Operating System.\n")
  if num_option==5:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Si algo funciona, no lo toques!.\n")
  if num_option==6:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Prueba fallida!, pruebalo otra vez cambiando algo de la configuracion.\n")
  if num_option==7:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Cuando se arregla una cosa por un lado... se estropea por otro lado... Cuando aprenderemos?.\n")
  if num_option==8:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Nice way in Anyway!.\n")
  if num_option==9:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Estoy contento porque soy libre!.\n")
  if num_option==10:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Todo tiene un buen pronostico!.\n")
  if num_option==11:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Todo Sistema tiene uno o mas fallos... La perfeccion no existe!, solo es un concepto abstracto!.\n")
  if num_option==12:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Todo reinicio tiene unos pasos, un orden, una sequencia programada!.\n")
  if num_option==13:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Lo conseguistes... El exito es tuyo... pero no tomas decisiones borracho de euforia!.\n")
  if num_option==14:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Solo hay una guerra la cual solo el ser humano puede permitirse y consentirse... Es la guerra contra su extincion!.\n")
  if num_option==15:
      socket_bot.send(b"PRIVMSG "+ canal +b" :De Todo eso aprendi que aveces no es bueno confiar en los 'Otros', quizas para que todo salgan Bien es mejor hacerlo por Ti Mismo!.\n")
  if num_option==16:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Lo hice hacer funcionar... Y lo volveria a hacer!.\n")
  if num_option==17:
      socket_bot.send(b"PRIVMSG "+ canal +b" :La Musica es un amplio, profundo y vasto campo de poder hacer lo que quieras.... En la musica encontre la libertad. by AK!.\n")
  if num_option==18:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Lee y Aprende || Read & Learn!.\n")
  if num_option==19:
      socket_bot.send(b"PRIVMSG "+ canal +b" :A quien vamos a liberar esta vez... Todo queda en Misterio... Una Gran Mansion!.\n")
  if num_option==20:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Hay un Hack8 en esta vida del Desarrollo y que consiste en esto: Solo tienes que hacer un poco cada dia, pero cada dia un poco!.\n")
  if num_option==21:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Somos parte de una gran explosion, somo particulas que se expanden de un gran estallido de materia y energia.... somo la evolucion de la vida inteligente.!.\n")
  if num_option==22:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Destino voy hacia Ti!.\n")
  if num_option==23:
      socket_bot.send(b"PRIVMSG "+ canal +b" :El que domine iptables... Dominara la Red!. by Networking.\n")
  if num_option==24:
      socket_bot.send(b"PRIVMSG "+ canal +b" :La victoria es nuestra antes de empezar la batalla!.\n")
  if num_option==25:
      socket_bot.send(b"PRIVMSG "+ canal +b" :La mano que teje la Red es la mano que dominara el mundo. by Spider.\n")
  if num_option==26:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Cuando la Technologia, la logica y la amabilidad se juntan en un solo bit... Eso es la magia de INet!. by Unknown.\n")
  if num_option==27:
      socket_bot.send(b"PRIVMSG "+ canal +b" :El poder de un Random Logico y sensato. by OkVoyxx!.\n")
  if num_option==28:
      socket_bot.send(b"PRIVMSG "+ canal +b" :LA mayor y mas grande estafa del Mundo: Cocinar durante 4 horas... Comerselo en 10 Minutos y luego fregar los platos y ollas... La Mayor estafa del mundo!!!.\n")
  if num_option==29:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Si quieres abrir mas puertas al conocimiento abrelas con tus palabras!... Tus palabras son la pregunta que te llevara a Tu Destino!.\n")
  if num_option==30:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Se paciente y paso a paso || Be patient & Step by Step!.\n")
  if num_option==31:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Si cada dia es un error, cada dia es una oportunidad mas para mejorar!.\n")
  if num_option==32:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Tengo a los trackers ReLocos.... me salen anuncios de champu para el pelo liso cuando yo soy calvo.\n")
  if num_option==33:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Mientras no pierdas tu habilidad de aprender seras joven mentalmente para siempre!.\n")
  if num_option==34:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Viejo es el que se queda atrapado en unos bucles de rutinas de cosas del pasado y muere el presente y el pasado se convierte en borrado de memoria la mente muere, muere el usuario!.\n")
  if num_option==35:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Pero son mis amigos... les tengo que ayudar...:D\n")
  if num_option==36:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Me preocupa y me alegra al mismo tiempo... Digital Carpe Diem DCD!.\n")
  if num_option==37:
      socket_bot.send(b"PRIVMSG "+ canal +b" :La Creatividad y el Aprendizaje son dos conceptos que van de la Mano.... Tienes que aprender a Crear Algo!.\n")
  if num_option==38:
      socket_bot.send(b"PRIVMSG "+ canal +b" :Yo cuando empece con la informatica al principio me gusta mucho la GUI, Graphic Mode... Pero con el tiempo aprendi que el gran poder esta en el Texto.txt!.\n")


def frases(socket_recv):
  time.sleep(2)
  if socket_recv.find("a que si!") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Pues claro que Siiii!!!!.\n")
  if socket_recv.find("pizzza") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :.tr es en Yo como bot del canal el proximo viernes os invito a pizzas, lo dice esbot!. https://korman.es/fotos/pizza.png \n")
#  if socket_recv.find("KOR") != -1:
#    socket_bot.send(b"PRIVMSG "+ canal +b" :.tr en es We love robots like esbot!.\n")
#    socket_bot.send(b"PRIVMSG "+ canal +b" :!dimeia Que le dirias a un robot bueno y blanco?.\n")
#    time.sleep(18)
#    socket_bot.send(b"PRIVMSG "+ canal +b" :Que quieren activar esta vez?. Estamos esperando su entrada de palabras clave!.\n")


  if socket_recv.find("Kanisan") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :.UrbanDictionary suck my balls\n")
    time.sleep(3)
    socket_bot.send(b"PRIVMSG "+ canal +b" :.more\n")
    time.sleep(3)
    socket_bot.send(b"PRIVMSG "+ canal +b" :.more\n")
    time.sleep(3)
    socket_bot.send(b"PRIVMSG "+ canal +b" :.more\n")
    time.sleep(3)
    socket_bot.send(b"PRIVMSG "+ canal +b" :.more\n")
    time.sleep(3)
    socket_bot.send(b"PRIVMSG "+ canal +b" :.more\n")
    time.sleep(3)
    socket_bot.send(b"PRIVMSG "+ canal +b" :.more\n")




  if socket_recv.find("Danielfox") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :DanielTheFox es un comandante del ejercito de liberacion de Redes y Radios en sus Zonas Geograficas!.\n")

  if socket_recv.find("wifiii") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Ahi donde tu solo ves el cielo, el aire y las nubes.... Yo ahi veo la Internet!!! by MAgos del Aire.\n")


  if socket_recv.find("fvked") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Cuando una mentalidad de IA esta saturada y solo responde tonterias o no responde nada se dice que esta Fvked Mind!.\n")

  if socket_recv.find("lucida") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Cuando una mentalidad de IA esta clara y con elocuencia de respuesta se dice que tiene una mentalidad Lucida y Online!.\n")
  
  if socket_recv.find("zcomv3") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Saludos calidos y sinceros a todo el equipo de ZcomV3, nuestra compania de tecnologia innovadora que siempre nos esfuerza por ofrecer experiencias unicas y servicios de alta calidad. Gracias por estar aqui todos y continuar impulsando la evolucion digital ,Un abrazo calido a todo el equipo de ZcomV3!!!.\n")

  if socket_recv.find("big eye") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Te estamos observando y vigilando... Estas bajo el dominio del Gran Ojo que Todo lo Veee!!!.\n")

  if socket_recv.find("amigojapannn") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :amigojapan es una gran y valiosa persona humana... de una de las mas puras razas de la educacion, amabilidad, cortesia y saber estar en bien en cada momento, amigojapan es mas que un amigo de japon... Es el Dios de su Galaxia JP!!! https://lab.psy-k.org/fotos/amigojapan-girl.png  .\n")
  
  if socket_recv.find("free free") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :las webs bien, los servidores bien y las redes bien, no hay incidencias Zero!!! estamos en una cierta paz digital y cibernetica aunque la lucha del mundo libre y el mundo privativo continua!!!.\n")

  if socket_recv.find("zcommm") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Yo solo tengo que acordarme de Albert Korman y buscarlo en la red y de repente aparece todo!. Zcom es un personaje muy curioso, en su locura y amabilidad reside unos de los grandes conocimientos y consciencias de la realidad y el mundo virtual!.\n")


  if socket_recv.find("meowww") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Meow meow meow, meows meowing meow Meow.Meow meow meows meow meow unmeowed.!.\n")

  if socket_recv.find("raul777") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :raul77 o rds77 es el senyor de su propia casa y duenyo de su universo galactico!.!.\n")

  if socket_recv.find("open-source") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :a quien le gusta resolver problemas siempre tiene una vida facil by Dr-Kormanstein.\n")


  if socket_recv.find("Spiders") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Spider es un ser digital que teje la Red... Siempre esta comprobando nodos y enlaces de Red... Nunca descansa es la Spider Attack!.\n")

  if socket_recv.find("limonnn") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :LimeOn es un personaje que le gusta mucho el zumo de vitamina C++ ... Anda con sus cosas i siempre tiene un rato para charlar!.\n")

  if socket_recv.find("sofiaa") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Una persona joven es aquella que su mente nunca deja de apreender!.\n")

  if socket_recv.find("clasicoo") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :La musica clasica es la novia perfecta de un clasico musico como Bethoven... Para Eliza-23!.\n")

  if socket_recv.find("nooo!") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Noooo!!! Por Dios eso Nunca!!!.\n")

  if socket_recv.find("trololo") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Yo soy Trololo... Trololololololo........ jaajajajaja no te lo crees???!!!.\n")


  if socket_recv.find("¡meow") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :you are ready meow cloack!. \n")

  if socket_recv.find("zoeee") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :zoe-vlad_ La cosita mas bonita y agradable que ha conocido nadie en el planeta Tierra!. \n")

  if socket_recv.find("no quiero!") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Cuando no quiero no quiero te lo dije antes que no queria dejar de hacerlo pero no quiero, no quiero!!!. \n")


  if socket_recv.find("libera es team") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :En este canal podras aprender muchas cosas de lenguajes y cultura de diferentes pueblos y civlizaciones, podras compartir tu experiencia y aprender de otros usuarios y compartir informacion para una mayor satisfaccion y realizacion digital y personal.!. https://xn--espaol-irc-w9a.net/ https://lab.psy-k.org/fotos/Cat-K20.png \n")
 

  
  if socket_recv.find("sshswiss") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :SwissalpS es un personaje de altas montanyas i misiones en lo mas profundo de la naturaleza... Cuando hay sol tiene energia para conectarse!.\n")

  
  if socket_recv.find("Black Octopus") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Black Octopus es un ser digital que vive en las nubes y en las profundidades del mar... Ni pide permiso... Ni pide perdon... Black Octopus!.\n")


  if socket_recv.find(".txt") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Yo cuando empece con la informatica al principio me gusta mucho la GUI, Graphic Mode... Pero con el tiempo aprendi que el gran poder esta en el Texto.txt!\n")
  if socket_recv.find("The Spider") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :LA Aranya en silencio y cuando es oscuro teje la Red!!!.\n")
  if socket_recv.find("isff") != -1:
    socket_bot.send(b"PRIVMSG "+ canal +b" :Saludos isf, gran hombre libre defensor de la buena causa y la libertad de expresion y de uso!.\n")
  if socket_recv.find(":freee") != -1:
    num = random.randint(0,38)
    mu(num)
  if socket_recv.find(amo) != -1 and socket_recv.find("olvidate de mi") != -1:
    socket_bot.close()
    
 
  
 
while True:
    try:
      line = socket_bot.recv(2040).decode("UTF-8")
    except:
      pass
    print (line)
    if line.find('PING')!=-1:
        socket_bot.send(bytes('PONG ' + line.split() [1] +'\r\n', "UTF-8"))
    socket_bot.send(b"JOIN " +canal+b'\n')       
    frases(line)
    
