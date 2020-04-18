#include <stdio.h>
#include <Windows.h>

unsigned char ptr[23] = { 0x7E, 0x01, 0x00, 0x00, 0x01, 0x10, 0x02, 0x00, 
                    0x27, 0x00, 0x0C, 0x00, 0x02, 0x00, 0x00, 0x00, 
                    0x00, 0x00, 0x50, 0x00, 0x3C, 0x00, 0x03 };

/*
* 函数名 :CRC16
* 描述 : 计算CRC16
* 输入 : ptr---数据,len---长度
* 输出 : 校验值
*/
unsigned short CRC16(unsigned char *ptr, unsigned short len)
{
    unsigned char i;
    unsigned short crc = 0xFFFF;
    if (len == 0) {
        len = 1;
    }
    while (len--) {
        crc ^= *ptr;
        for (i = 0; i<8; i++)
        {
            if (crc & 1) {
                crc >>= 1;
                crc ^= 0xA001;
            } else {
                crc >>= 1;
            }
        }
        ptr++;
    }
    return(crc);
}

int main()
{
    printf("%04x\n", CRC16(ptr, 23));
    getchar();
}
