package pelota;
 
 
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ConcurrentModificationException;
import java.util.Vector;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.swing.JComponent;
import javax.swing.JOptionPane;
 
/**
 *
 * @author Yacoobs
 * Viernes 17 de noviembre de 2017.
 * 
 * Programa muy sencillo basado en el famoso juego de hacer rebotar una pelota e ir eliminando todos los ladrillos
 * que hay en el mapa, estos de dan puntos a cambio. Dispones de un determinado numero de vidas si la bola cae por 
 * debajo de tu plataforma.
 */
public class Interface_Juego extends javax.swing.JFrame {
 
    private boolean Tocar_Bola = true;
    private boolean Empezar = false;
    private boolean findeljuego=false;
 
 
    private int Suma_puntos = 5;
    private int Puntos = 0;
    private int Posicion_BolaX;
    private int Posicion_BolaY;
    private int Posicion_BarraX;
    private float velocidad = 2.8f;
    private int tamano = 20;
    private int X=1;
    private int Y=1;
    private int vidas = 3;
 
    private Vector<Integer> Columna1 = new Vector<>();
    private Vector<Integer> Columna2 = new Vector<>();
    private Vector<Integer> Columna3 = new Vector<>();
    private Vector<Integer> Columna4 = new Vector<>();
    private Vector<Integer> Columna5 = new Vector<>();
    private Vector<Integer> Columna6 = new Vector<>();
 
    private ReproducirAudio ReAudio;
    private BufferedImage ImgBuff, PelotaBuff, BarraBuff, Degradado1, Degradado2, Degradado3, Degradado4;
 
 
 
 
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">                          
    private void initComponents() {
 
        jPanel_Opciones = new javax.swing.JPanel();
        jLabel_vidas = new javax.swing.JLabel();
        jLabel_Puntos = new javax.swing.JLabel();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel_Fondo = new javax.swing.JLabel();
        jMenuBar1 = new javax.swing.JMenuBar();
        jMenu1 = new javax.swing.JMenu();
        jMenuItem1 = new javax.swing.JMenuItem();
 
        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setBackground(new java.awt.Color(0, 0, 0));
        setResizable(false);
        addMouseMotionListener(new java.awt.event.MouseMotionAdapter() {
            public void mouseMoved(java.awt.event.MouseEvent evt) {
                formMouseMoved(evt);
            }
        });
        addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                formMousePressed(evt);
            }
        });
 
        jPanel_Opciones.setBackground(new java.awt.Color(0, 0, 0));
        jPanel_Opciones.setForeground(new java.awt.Color(255, 255, 255));
        jPanel_Opciones.setPreferredSize(new java.awt.Dimension(788, 70));
        jPanel_Opciones.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());
 
        jLabel_vidas.setFont(new java.awt.Font("Vani", 1, 24)); // NOI18N
        jLabel_vidas.setForeground(new java.awt.Color(255, 255, 255));
        jLabel_vidas.setText("Vidas :");
        jPanel_Opciones.add(jLabel_vidas, new org.netbeans.lib.awtextra.AbsoluteConstraints(50, 20, -1, -1));
 
        jLabel_Puntos.setFont(new java.awt.Font("Vani", 1, 24)); // NOI18N
        jLabel_Puntos.setForeground(new java.awt.Color(255, 255, 255));
        jLabel_Puntos.setText("Puntos:");
        jPanel_Opciones.add(jLabel_Puntos, new org.netbeans.lib.awtextra.AbsoluteConstraints(270, 20, -1, -1));
 
        jLabel1.setForeground(new java.awt.Color(204, 0, 0));
        jLabel1.setText("X");
        jPanel_Opciones.add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(810, 10, -1, -1));
 
        jLabel2.setForeground(new java.awt.Color(255, 0, 51));
        jLabel2.setText("Y");
        jPanel_Opciones.add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(810, 40, -1, -1));
        jPanel_Opciones.add(jLabel_Fondo, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 900, 70));
 
        getContentPane().add(jPanel_Opciones, java.awt.BorderLayout.PAGE_START);
 
        jMenu1.setText("Menu");
 
        jMenuItem1.setText("Reiniciar");
        jMenuItem1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jMenuItem1ActionPerformed(evt);
            }
        });
        jMenu1.add(jMenuItem1);
 
        jMenuBar1.add(jMenu1);
 
        setJMenuBar(jMenuBar1);
 
        pack();
    }// </editor-fold>                        
 
    //Constructor del programa..........
    public Interface_Juego() {
 
        setTitle("Rompe Ladrillos V.0.1");
 
        initComponents();
 
        Iniciar();
 
        //Abrimos y cargamos las imagenes de dibujado del programa.....
        try {
            ImgBuff = ImageIO.read(new File("FondoJuego/FondoJuego_Cubos.jpg").getAbsoluteFile());
            PelotaBuff = ImageIO.read(new File("Graficos/Pelota.png").getAbsoluteFile());
            BarraBuff = ImageIO.read(new File("Graficos/Barra.png").getAbsoluteFile());
            Degradado1 = ImageIO.read(new File("Graficos/degradado1.jpg").getAbsoluteFile());
            Degradado2 = ImageIO.read(new File("Graficos/degradado2.jpg").getAbsoluteFile());
            Degradado3 = ImageIO.read(new File("Graficos/degradado3.jpg").getAbsoluteFile());
            Degradado4 = ImageIO.read(new File("Graficos/degradado4.jpg").getAbsoluteFile());
        }
        catch (IllegalArgumentException ex) {
            JOptionPane.showMessageDialog(this, "Error1 " + ex,"Error",1);}
        catch (IOException ex) {
            JOptionPane.showMessageDialog(this, "Error2 " + ex,"Error",1);}
 
        //Llamamos a la clase paint para introducir al Frame.
        add(new Introduce_Graficos());
 
        jLabel_vidas.setText("Vidas: " + vidas);
 
        setBounds(100, 100, 900, 850);
 
        ReAudio = new ReproducirAudio();
 
        ReAudio.Reproducir("Efecto1.mp3");
 
    }
 
    //Clase Interna encargada del la parte Grafica del juego....
    public class Introduce_Graficos extends JComponent{
 
        @Override
        public  void paint(java.awt.Graphics g){
 
            Graphics2D g2 = (Graphics2D) g;
 
            //Dibujamos un Fondo de Imagen del juego...
            g2.drawImage(ImgBuff, 0, 0,this);
 
            DibujarMapa(g2, Columna1, Degradado3, 50);
            DibujarMapa(g2, Columna2, Degradado2, 80);
            DibujarMapa(g2, Columna3, Degradado2, 110);
            DibujarMapa(g2, Columna4, Degradado1, 140);
            DibujarMapa(g2, Columna5, Degradado4, 170);
            DibujarMapa(g2, Columna6, Degradado4, 200);
 
            //Dibuja la Pelota Grafica...
            if (Empezar){
                g2.drawImage(PelotaBuff, Posicion_BolaX, Posicion_BolaY,this);
            }else{
                g2.drawImage(PelotaBuff, Posicion_BarraX+40, 650,this);
            }
 
            if (vidas==0){
 
                g2.setColor(Color.red);
                g2.setFont(new Font("Blackoak Std", Font.BOLD, 30));
                g2.drawString("Fin del Juego",200, 400);
                if (!Empezar){
                    ReAudio.Reproducir("Fin_del_Juego.mp3");
                    Empezar=true;
                }
            }
 
            if (findeljuego && vidas!=0){
                g2.setColor(Color.BLUE);
                g2.setFont(new Font("Blackoak Std", Font.BOLD, 30));
                g2.drawString("Mapa Completado",150, 400);
            }
 
            //Dibuja la Barra de movimiento....
            g2.drawImage(BarraBuff, Posicion_BarraX, 670,this);
 
 
            //Dibuja el Perimetro de Paredes del juego...
            g2.setColor(Color.red);
            g2.setStroke(new BasicStroke(5));
            g2.drawRect(0, 0, getWidth(), getHeight()+20);
        }
    }
 
 
    //Eventos a la escucha del programa.....
    private void formMousePressed(java.awt.event.MouseEvent evt) {
        // TODO add your handling code here:
 
        if (!Empezar && !findeljuego){
            System.out.println("Empezar");
            Jugar();
            Empezar=true;
            Posicion_BolaX = Posicion_BarraX+40;
            Posicion_BolaY = 650;
        }
    }
 
    private void formMouseMoved(java.awt.event.MouseEvent evt) {
        // TODO add your handling code here:
 
 
        int X= evt.getX();
 
        Posicion_BarraX = X-50;
 
        if (X<55){
            Posicion_BarraX=5;
        }
 
        if (X>getWidth()-57){
            Posicion_BarraX=getWidth()-107;
        }
 
        repaint();
 
    }
 
    private void jMenuItem1ActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO Iniciamos el juegos desde 0:
 
        findeljuego=true;
        vidas=0;
        Empezar=true;
 
        Columna1.clear();
        Columna2.clear();
        Columna3.clear();
        Columna4.clear();
        Columna5.clear();
 
        Iniciar();
        findeljuego=false;
        Puntos=0;
        vidas=3;
        Empezar=false;
 
 
 
    }
 
 
 
    //Metodos del Programa....................
 
    public void Iniciar(){
        //Llamamos a este metodo que nos ayuda a crear la estructura del mapa.
        CrearEstructura_Mapa(Columna1, 5, 850, 52);
        CrearEstructura_Mapa(Columna2, 100, 760, 55);
        CrearEstructura_Mapa(Columna3, 100, 760, 55);
        CrearEstructura_Mapa(Columna4, 100, 760, 55);
        CrearEstructura_Mapa(Columna5, 40, 800, 60);
        CrearEstructura_Mapa(Columna6, 160, 700, 60);
 
 
    }
 
    public void DibujarMapa(Graphics2D g2, Vector<Integer> vector,BufferedImage Imagen, int Altura){
 
        for (int dat:vector){
            g2.drawImage(Imagen,dat, Altura, this);
 
        }
    }
 
    public void Evaluar(){
 
        Posicion_BolaX +=X;
        Posicion_BolaY +=Y;
 
        Rectangle Espacio_Bola = new Rectangle(Posicion_BolaX, Posicion_BolaY, tamano, tamano);
        Rectangle Espacio_Barra = new Rectangle(Posicion_BarraX, 670, 100, 15);
 
 
        if (Espacio_Bola.intersects(Espacio_Barra) && Tocar_Bola){
 
            Y = -Y;
            Tocar_Bola=false;
            ReAudio.Reproducir("Efecto1.mp3");
 
        }else{
 
            EliminarBloques(Espacio_Bola, Columna1,50);
            EliminarBloques(Espacio_Bola, Columna2,80);
            EliminarBloques(Espacio_Bola, Columna3,110);
            EliminarBloques(Espacio_Bola, Columna4,140);
            EliminarBloques(Espacio_Bola, Columna5,170);
            EliminarBloques(Espacio_Bola, Columna6,200);
 
            if (Posicion_BolaX<0){
                X = -X;
                Tocar_Bola=true;
                ReAudio.Reproducir("Efecto2.mp3");
            }
            if (Posicion_BolaY<0){
                Y = -Y;
                Tocar_Bola=true;
                ReAudio.Reproducir("Efecto2.mp3");
            }
            if (Posicion_BolaX>getWidth()-28){
                X = -X;
                Tocar_Bola=true;
                ReAudio.Reproducir("Efecto2.mp3");
            }
            if (Posicion_BolaY>getHeight()-100){
 
                ReAudio.Reproducir("Efecto3.mp3");
                vidas=vidas-1;
                jLabel_vidas.setText("Vidas: " + vidas);
                Empezar=false;
                Tocar_Bola=true;
 
                if (vidas==0){
                    findeljuego=true;
                }
            }
 
            jLabel1.setText("X: "+X);
            jLabel2.setText("Y: "+Y);
 
        }
    }
 
    public void EliminarBloques(Rectangle Espacio_Bola, Vector<Integer> Cuadrado, int altura){
 
        try{
            int x=0;
            for (int dat:Cuadrado){
 
                Rectangle cuadrado1 = new Rectangle(dat, altura, 50, 20);
 
                if (Espacio_Bola.intersects(cuadrado1)){
 
                    Y = -Y;
 
                    Tocar_Bola=true;
                    ReAudio.Reproducir("Efecto5.mp3");
                    Cuadrado.remove(x);
                    Puntos = Puntos + Suma_puntos;
                    jLabel_Puntos.setText("Puntos: " + Puntos);
 
                }
                x++;
            }
 
            }catch(ConcurrentModificationException e){
                //Logger.getLogger(Interface_Juego.class.getName()).log(Level.SEVERE, null, e);
            }
 
    }
 
    public void Jugar(){
 
        Thread hilo = new Thread(new Runnable() {
 
                @Override
                public void run() {
 
                    while (Empezar && vidas!=0 && !findeljuego){
 
                        int C1 = Columna1.size();
                        int C2 = Columna2.size();
                        int C3 = Columna3.size();
                        int C4 = Columna4.size();
                        int C5 = Columna5.size();
                        int C6= Columna6.size();
 
                        if (C1==0 && C2==0 && C3==0 && C4==0 && C5==0 && C6==0){
                            findeljuego=true;
                            ReAudio.Reproducir("Efecto6.mp3");
                            repaint();
                        }
 
 
                        try {
                            Thread.sleep((long) velocidad);
                        } catch (InterruptedException ex) {
                            Logger.getLogger(Interface_Juego.class.getName()).log(Level.SEVERE, null, ex);
                        }
 
                        Evaluar();
                        repaint();
                    }
 
                }
 
            });
       hilo.start();
    }
 
    public void CrearEstructura_Mapa(Vector<Integer> vector, int Principio, int Final, int Separacion){
 
        for (int x=Principio;x<Final;x+=Separacion){
            vector.add(x);
        }
    }
 
 
 
 
 
 
 
    //Parte de inicio del programa....................
    public static void main(String args[]) {
 
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Interface_Juego().setVisible(true);
            }
        });
    }
 
    // Variables declaration - do not modify                     
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel_Fondo;
    private javax.swing.JLabel jLabel_Puntos;
    private javax.swing.JLabel jLabel_vidas;
    private javax.swing.JMenu jMenu1;
    private javax.swing.JMenuBar jMenuBar1;
    private javax.swing.JMenuItem jMenuItem1;
    private javax.swing.JPanel jPanel_Opciones;
    // End of variables declaration                   
}
 
 
 
 
 
 
 
 
 
 
//Clase de Reproduccion de audio............
 
package pelota;
 
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import javax.swing.JOptionPane;
import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.Player;
 
 
 
/**
 * @author Yacoobs
 * Esta clase se encarga de reproducir efectos de audio del programa 
 * Precisa de la libreria externa Jl1.0.jar JLayer 1.0.1 
 * Descarga: http://www.java2s.com/Code/Jar/j/Downloadjl10jar.htm
 */
public class ReproducirAudio {
 
    private Player sonido;
    private File file=null;
 
    //Metodo encargado de reproducir el audio, pide la ruta y el nombre de archivo para reproducir el audio.
    public void Reproducir(String ruta){
 
        if (ruta!=""){
 
            Thread EmpezarAudio = new Thread(new Runnable() {
                @Override
                public void run() {
 
                    try {
                        file = new File("").getAbsoluteFile();
 
 
                    } catch(NullPointerException e2){
                        System.out.println("Error la ruta o archivo no encontrado de audio....");
                    }
 
                    try {
 
                        InputStream inputStream = new FileInputStream(file + "/Audio/" + ruta);
 
                        sonido = new Player(inputStream);
 
                        sonido.play();
 
                    } catch (JavaLayerException e) {
                        JOptionPane.showMessageDialog(null, "Error Reproducir Audio JavaLayerException \n" + e);
                    } catch (FileNotFoundException e) {
 
                        JOptionPane.showMessageDialog(null, "Error Reproducir Audio FileNotFoundException \n" + e);
                    } catch (NullPointerException e){
 
                        JOptionPane.showMessageDialog(null, "Error Reproducir Audio showMessageDialog \n" + e);
                    }
                }
            });
            EmpezarAudio.start();
        }
    }
 
    //Metodo utilizado para detener el audio.
    public void detener(){
        sonido.close();
    }
 
 
}