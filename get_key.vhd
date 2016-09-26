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
signal signal1     : std_logic;
signal enable      : std_logic;
signal shift_reg   : std_logic_vector(9 downto 0);
signal key_o       : std_logic_vector(7 downto 0);
signal count       : std_logic_vector(3 downto 0);
signal key_valid_c : std_logic;
signal key_valid_o : std_logic;
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
      key_valid_c <= '0';
   elsif(falling_edge(clk)) then
      if(count = "1001") then
         count <= "0000";
         key_valid_c <= '1';
      else
         count <= count + 1;
      end if;
   end if;
end process;

--letch output signals key_valid
process(clk, reset)
begin
	if(reset = '0') then
		key_valid_o <= '0';
	elsif(falling_edge(clk)) then
		key_valid_o <= key_valid_c;
	end if;
end process;

--letch output signal key (8b)
process(clk, reset)
begin
	if(reset = '0') then
        key_o <= (others =>'0');
   elsif(falling_edge(clk)) then
        key_o <= shift_reg(9 downto 2);
	end if;
end process;

key_valid <= key_valid_o;
key <= key_o;
end architecture behavioral;
