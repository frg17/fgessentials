using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class UDPListener {
    private const int listenPort = 11000;

    public delegate int Del(string message);

    static private int isSame(string str) {
        return String.Compare("Lil bitch!", str);
    }

    public static void StartListener(Object obj) {
        Del del = (Del) obj;

        UdpClient listener = new UdpClient(listenPort);
        IPEndPoint groupEP = new IPEndPoint(IPAddress.Any, listenPort);

        try {
            while(true) {
                byte[] bytes = listener.Receive(ref groupEP);
                
                if(del(Encoding.ASCII.GetString(bytes, 0, bytes.Length)) == 0)
                    Console.WriteLine("Oh shiiiiiit! That boi just called you a lil biiiitch");
            }
        } catch (SocketException e) {
            Console.WriteLine(e);
        } finally {
            listener.Close();
        }
    }

    public static void Main() {
    }
}