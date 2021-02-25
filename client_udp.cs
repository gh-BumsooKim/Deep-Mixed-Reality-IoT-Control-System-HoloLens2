using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;

public class Socket_01 : MonoBehaviour
{
    public void socket_client()
    {
        Socket client = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
        var data = Encoding.UTF8.GetBytes("Hello");
        client.SendTo(data, new IPEndPoint(IPAddress.Parse("192.168.0.11"), 43210));
        client.Close();
        Debug.Log(Encoding.UTF8.GetString(data));
    }
}
