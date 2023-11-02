import timeout
import error
import check_buff
import size_buff

if __name__ == '__main__':
    print("Executing timeout.py")
    timeout.test_socket_timeout()
    print("\nExecuting error.py")
    error.main()
    print("\nExecuting check_buff.py")
    check_buff.get_default_buffer_size()
    print("\nExecuting size_buff.py")
    size_buff.modify_buff_size()
    