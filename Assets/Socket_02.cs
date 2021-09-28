using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;

public class Socket_02 : MonoBehaviour
{
    
    public void socket_client()
    {
        /*
        Socket client = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        client.Connect(new IPEndPoint(IPAddress.Parse("192.168.0.11"), 43210));

        var data = Encoding.UTF8.GetBytes("Hello");

        //client.Send(BitConverter.GetBytes(data.Length));
        client.Send(data);

        data = new byte[4];
        //client.Receive(data, data.Length, SocketFlags.None);
        //Array.Reverse(data);
        //data = new byte[BitConverter.ToInt32(data, 0)];
        client.Receive(data, data.Length, SocketFlags.None);
        Debug.Log(Encoding.UTF8.GetString(data));
        */

        Socket client = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
        var data = Encoding.UTF8.GetBytes("Stop");
        client.SendTo(data, new IPEndPoint(IPAddress.Parse("192.168.0.17"), 43210));
        client.SendTo(data, new IPEndPoint(IPAddress.Parse("192.168.0.11"), 43210));
        client.Close();
        Debug.Log(Encoding.UTF8.GetString(data));
    }


}
