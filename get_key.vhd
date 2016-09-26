library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity get_key is
port(
--input signals

--information signals
ps2_clk  : in std_logic;
ps2_data : in std_logic;

--clock and reset signals
clk      : in std_logic;
reset    : in std_logic;

--output signals
key       : out std_logic_vector(7 downto 0); --8b key
key_valid : out std_logic                     --key is valid when key_valid is '1'
);
end entity get_key;

architecture behavioral of get_key is
signal signal1 : std_logic;
signal enable : std_logic;
signal shift_reg : std_logic_vector(9 downto 0);
signal count : std_logic_vector(3 downto 0);
begin

--detect falling edge od ps2_clk
process(clk, reset)
begin
   if(reset = '0') then
      signal1 <= '0';
   elsif(falling_edge(clk)) then
      signal1 <= ps2_clk;
   end if;
end process;
enable <= (not ps2_clk) and signal1;

--10b shift register for key detection
process(clk,reset)
begin
   if(reset = '0') then
      shift_reg <= (others=>'0');
   elsif(falling_edge(clk) and (enable = '1')) then
      shift_reg(8 downto 0) <= shift_reg(9 downto 1);
      shift_reg(9) <= ps2_data;
   end if;
end process;

--counter
process(clk, reset)
begin
   if(reset = '0') then
      count <= "0000";
      key_valid <= '0';
      key <= (others => '0');
   elsif(falling_edge(clk)) then
      if(count = "1010") then
         count <= "0000";
         key_valid <= '1';
         key <= shift_reg(9 downto 2);
      else
         count <= count + 1;
      end if;
   end if;
end process;
end architecture behavioral;
