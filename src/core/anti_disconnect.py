# JavaScript Heartbeat giữ phiên làm việc Colab không bị ngắt kết nối
JS_HEARTBEAT_CODE = """
function ConnectButton(){
    console.log("Connect pushed"); 
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click() 
}
setInterval(ConnectButton, 60000);
"""
