STC3100_REG_MODE = 0x00 #Mode Register

#define STC3100_REG_CTRL                 0x01 /*Control and Status Register   */
#define STC3100_REG_CHARGE_LOW           0x02 /*Gas Gauge Charge Data Bits 0-7*/
#define STC3100_REG_CHARGE_HIGH          0x03 /*Gas Gauge Charge Data Bits 8-15*/    
#define STC3100_REG_COUNTER_LOW          0x04 /*Number of Conversion Bits 0-7*/
#define STC3100_REG_COUNTER_HIGH         0x05 /*Number of Conversion Bits 8-15*/
#define STC3100_REG_CURRENT_LOW          0x06 /*Battery Current Value Bits 0-7*/
#define STC3100_REG_CURRENT_HIGH         0x07 /*Battery Current Value Bits 8-15*/
#define STC3100_REG_VOLTAGE_LOW          0x08 /*Battery Voltage Value Bits 0-7*/
#define STC3100_REG_VOLTAGE_HIGH         0x09 /*Battery Voltage Value Bits 8-15*/
#define STC3100_REG_TEMPERATURE_LOW      0x0A /*Temperature Values Bits 0-7) */
#define STC3100_REG_TEMPERATURE_HIGH     0x0B /*Temperature Values Bits 8-15)*/

#define STC3100_REG_ID0                  0x18 /*Part Type ID 10h  */
#define STC3100_REG_ID1                  0x19 /*Unique Part ID Bits 0-7  */
#define STC3100_REG_ID2                  0x1A /*Unique Part ID Bits 8-15  */
#define STC3100_REG_ID3                  0x1B /*Unique Part ID Bits 16-23  */
#define STC3100_REG_ID4                  0x1C /*Unique Part ID Bits 24-31  */
#define STC3100_REG_ID5                  0x1D /*Unique Part ID Bits 32-39  */
#define STC3100_REG_ID6                  0x1E /*Unique Part ID Bits 40-47  */
#define STC3100_REG_ID7                  0x1F /*Device ID CRC  */

#define STC3100_RAM_SIZE                 32  /*Total RAM register of STC3100*/

#define STC3100_REG_RAM0                               0x20  
#define STC3100_REG_RAM2                               0x22
#define STC3100_REG_RAM4                               0x24
#define STC3100_REG_RAM6                               0x26
#define STC3100_REG_RAM8                               0x28  
#define STC3100_REG_RAM12                              0x2C  
#define STC3100_REG_RAM14                              0x2E  
#define STC3100_REG_RAM16                              0x30  
#define STC3100_REG_RAM18                              0x32 
#define STC3100_REG_RAM20                              0x34 
#define STC3100_REG_RAM22                              0x36 
#define STC3100_REG_RAM24                              0x38 
#define STC3100_REG_RAM26                              0x3A 
#define STC3100_REG_RAM28                              0x3C 
#define STC3100_REG_RAM30                              0x3E 
