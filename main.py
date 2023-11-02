import timeout
import socketerror
import modif_buffer
import buffer

if __name__ == '__main__':
    print("Executing timeout.py")
    timeout.test_socket_timeout()
    print("\nExecuting socketerror.py")
    socketerror.main()
    print("\nExecuting buffer.py")
    buffer.get_default_buffer_size()
    print("\nExecuting modif_buffer.py")
    modif_buffer.modify_buff_size()