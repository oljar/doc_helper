from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import inspect
from search_module import blade_runner as word
from search_module import *
import re
#

class Application(Frame):


    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.pack()
        self.number = 0
        self.count()
        self.solution=word()
        self.identity_frame()
        self.supply_frame()
        self.vent_supply_frame()

        self.exhaust_frame()
        self.heater_frame()
        self.cooler_frame()
        self.vent_exhaust_frame()

        self.pre_filter_supply_01_frame()
        self.pre_filter_supply_02_frame()
        self.second_filter_supply_01_frame()
        self.second_filter_supply_02_frame()
        self.third_filter_supply_01_frame()
        self.third_filter_supply_02_frame()
        self.pre_filter_exhaust_01_frame()
        self.pre_filter_exhaust_02_frame()
        self.second_filter_exhaust_01_frame()
        self.second_filter_exhaust_02_frame()
        self.third_filter_exhaust_01_frame()
        self.third_filter_exhaust_02_frame()
        self.counterflow_frame()
        self.heat_rec_frame()
        self.mass_frame()
        self.group_various()
        self.get_method_SV()




    def count(self):

        self.number= self.number + 1
        print (self.number)
        yield self.number


    def lba_identity(self,X,Y,txt):
         return ttk.Label(self.lframe_identity, text=txt).grid(column=X, row=Y + 1,pady=(1, 10), padx=10,sticky=W)


    def project(self,X=0,Y=1):

        self.value_project_no = StringVar()
        self.value_project_no.set(self.solution[self.count().__next__()])
        self.entry_project = ttk.Entry(self.lframe_identity, textvariable=self.value_project_no).grid(column=X, row=Y )
        self.lba_identity(X,Y,txt="Symbol projektu")


    def order(self,X=0,Y=10):
        self.value_order_no = StringVar()
        self.value_order_no.set(self.solution[self.count().__next__()])

        self.entry_order = ttk.Entry(self.lframe_identity, textvariable=self.value_order_no).grid(column=X, row=Y,padx=10)

        self.lba_identity(X, Y, txt="Zamówienie")


    def serial_number(self,X=20,Y=10):

        self.value_se_num = StringVar()
        self.value_se_num.set(self.solution[self.count().__next__()])

        self.entry_se_num = ttk.Entry(self.lframe_identity, textvariable=self.value_se_num).grid(column = X,row = Y , padx=10 )

        self.lba_identity(X, Y, txt="Numer seryjny")


    def model(self,X=30,Y=10):

        self.value_model_symbol = StringVar()

        self.value_model_symbol.set(self.solution[self.count().__next__()])

        self.entry_model = ttk.Entry(self.lframe_identity, textvariable=self.value_model_symbol).grid(column=X, row=Y, padx=10 )

        self.lba_identity(X, Y, txt="Model")



    def system(self,X=40,Y=10):

        self.value_system_symbol = StringVar()

        self.value_system_symbol.set(self.solution[self.count().__next__()])

        self.entry_system = ttk.Entry(self.lframe_identity, textvariable=self.value_system_symbol).grid(column=X, row=Y, padx=10 )

        self.lba_identity(X, Y, txt="System")




    def identity_frame(self):
        self.lframe_identity = ttk.LabelFrame(tab_1, text="Identyfikacja")
        self.lframe_identity.pack()

        self.project()
        self.order()
        self.serial_number()
        self.model()
        self.system()



########################################################################################################################


    def lba_supply(self,X,Y,txt):
         return ttk.Label(self.lframe_supply, text=txt).grid(column=X, row=Y + 1,pady=(1, 10), padx=10,sticky=W)


    def performance_supply(self,X=0,Y=0):

        self.value_supply_symbol = StringVar()

        self.value_supply_symbol.set(self.solution[self.count().__next__()]+' ' + self.solution[self.count().__next__()]+' '+ self.solution[self.count().__next__()].upper())

        self.entry_perf_supply = ttk.Entry(self.lframe_supply, textvariable=self.value_supply_symbol).grid(column=X, row=Y, padx=10)

        self.lba_supply(X, Y, txt="Wykonanie - symbol")


    def output_supply(self,X=10,Y=0):

        self.value_output_supply = StringVar()

        self.value_output_supply.set(self.solution[self.count().__next__()])

        self.entry_output_supply = ttk.Entry(self.lframe_supply, textvariable=self.value_output_supply).grid(column=X, row=Y)

        self.lba_supply(X, Y, txt="Wydatek [m3/h]")



    def pressure_supply(self,X=20,Y=0):


        self.value_pressure_supply = StringVar()

        self.value_pressure_supply.set(self.solution[self.count().__next__()])

        self.entry_pressure_supply = ttk.Entry(self.lframe_supply, textvariable=self.value_pressure_supply).grid(column=X, row=Y )

        self.lba_supply(X, Y, txt="Spręż dyspozycyjny [Pa]")

    def supply_frame(self):
        self.lframe_supply = ttk.LabelFrame(tab_2, text="Nawiew")
        self.lframe_supply.pack()
        self.performance_supply()
        self.output_supply()
        self.pressure_supply()

#####################################################################################################################################

    def lba_vent_supply(self, X, Y, txt):
        return ttk.Label(self.lframe_vent_supply, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)


    def type_vent_supply(self, X=0, Y=0):

        self.value_vent_supply_symbol = StringVar()
        self.value_vent_supply_symbol.set(self.solution[self.count().__next__()])
        self.entry_supply = ttk.Entry(self.lframe_vent_supply, textvariable=self.value_vent_supply_symbol).grid(column=X, row=Y, padx=10)
        self.lba_vent_supply(X, Y + 10, txt="Symbol")


    def power_vent_supply(self, X=0, Y=20):
        self.value_power_supply = StringVar()
        self.value_power_supply.set(self.solution[self.count().__next__()])
        self.entry_power_supply = ttk.Entry(self.lframe_vent_supply, textvariable=self.value_power_supply).grid(column=X, row=Y, padx=10)
        self.lba_vent_supply(X, Y + 10, txt="Moc [kW]")

    def current_vent_supply(self, X=0, Y=40):
        self.value_current_supply = StringVar()
        self.value_current_supply.set(self.solution[self.count().__next__()])
        self.entry_current_supply = ttk.Entry(self.lframe_vent_supply, textvariable=self.value_current_supply).grid(column=X, row=Y, padx=10)
        self.lba_vent_supply(X, Y + 10, txt="Prąd [A]")

    def rotation_vent_supply(self, X=0, Y=60):
        self.value_rotation_supply = StringVar()
        self.value_rotation_supply.set(self.solution[self.count().__next__()])
        self.entry_rotation_supply = ttk.Entry(self.lframe_vent_supply, textvariable=self.value_rotation_supply).grid(column=X, row=Y, padx=10)
        self.lba_vent_supply(X, Y + 10, txt="Obroty [1/min]")

    def voltage_vent_supply(self, X=0, Y=80):
        self.value_voltage_supply = StringVar()
        self.value_voltage_supply.set(self.solution[self.count().__next__()])
        self.entry_voltage_supply = ttk.Entry(self.lframe_vent_supply, textvariable=self.value_voltage_supply).grid(column=X, row=Y, padx=10)
        self.lba_vent_supply(X, Y + 10, txt="Napięcie [V]")

    def frequency_vent_supply(self, X=0, Y=100):
        self.value_frequency_supply = StringVar()
        self.value_frequency_supply.set(self.solution[self.count().__next__()])
        self.entry_frequency_supply = ttk.Entry(self.lframe_vent_supply, textvariable=self.value_frequency_supply).grid(column=X, row=Y, padx=10)
        self.lba_vent_supply(X, Y + 10, txt="Częstotliwość [Hz]")
##################################################################################################################################################

    def vent_supply_frame(self):
        self.lframe_vent_supply = ttk.LabelFrame(tab_2, text="sekcja wentylatora - Nawiew")
        self.lframe_vent_supply.pack()
        self.type_vent_supply()
        self.power_vent_supply()
        self.current_vent_supply()
        self.rotation_vent_supply()
        self.voltage_vent_supply()
        self.frequency_vent_supply()



    ##################################################################################################################################################

    def lba_exhaust(self, X, Y, txt):
        return ttk.Label(self.lframe_exhaust, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)

    def performance_exhaust(self, X=0, Y=0):
        self.value_exhaust_symbol = StringVar()
        self.value_exhaust_symbol.set(self.solution[self.count().__next__()])
        self.entry_perf_exhaust = ttk.Entry(self.lframe_exhaust, textvariable=self.value_exhaust_symbol).grid(column=X, row=Y, padx=10)
        self.lba_exhaust(X, Y, txt="Wykonanie - symbol")

    # textvariable=self.value_output_exhaust

    def output_exhaust(self, X=10, Y=0):
        self.value_output_exhaust = StringVar()
        self.value_output_exhaust.set(self.solution[self.count().__next__()])
        self.entry_output_exhaust = ttk.Entry(self.lframe_exhaust, textvariable=self.value_output_exhaust).grid(
            column=X, row=Y)
        self.lba_exhaust(X, Y, txt="Wydatek [m3/h]")

    def pressure_exhaust(self, X=20, Y=0):
        self.value_pressure_exhaust = StringVar()
        self.value_pressure_exhaust.set(self.solution[self.count().__next__()])
        self.entry_pressure_supply = ttk.Entry(self.lframe_exhaust, textvariable=self.value_pressure_exhaust).grid(
            column=X, row=Y)
        self.lba_exhaust(X, Y, txt="Spręż dyspozycyjny [Pa]")

    def exhaust_frame(self):
        self.lframe_exhaust = ttk.LabelFrame(tab_3, text="Wywiew ")
        self.lframe_exhaust.pack()
        self.performance_exhaust()
        self.output_exhaust()
        self.pressure_exhaust()

#######################################################################################################################

    def lba_vent_exhaust( self,X,Y,txt):
        return ttk.Label(self.lframe_vent_exhasut, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)

    def type_vent_exhaust(self, X=0, Y=0):
        self.value_vent_exhaust_symbol = StringVar()
        self.value_vent_exhaust_symbol.set(self.solution[self.count().__next__()])
        self.entry_perf_exhaust = ttk.Entry(self.lframe_vent_exhasut, textvariable=self.value_vent_exhaust_symbol).grid(column=X, row=Y, padx=10)
        self.lba_vent_exhaust(X, Y+10, txt="Symbol" )

    def power_vent_exhaust(self, X=0, Y=20):
        self.value_power_vent_exhaust = StringVar()
        self.value_power_vent_exhaust.set(self.solution[self.count().__next__()])
        self.entry_power_vent_exhaust = ttk.Entry(self.lframe_vent_exhasut, textvariable=self.value_power_vent_exhaust).grid(column=X, row=Y, padx=10)
        self.lba_vent_exhaust(X, Y + 10, txt="Moc [kW]")

    def current_vent_exhaust(self, X=0, Y=40):
        self.value_current_vent_exhaust = StringVar()
        self.value_current_vent_exhaust.set(self.solution[self.count().__next__()])
        self.entry_current_vent_exhaust = ttk.Entry(self.lframe_vent_exhasut, textvariable=self.value_current_vent_exhaust).grid(column=X, row=Y, padx=10)
        self.lba_vent_exhaust(X, Y + 10, txt="Prąd [A]")

    def rotation_vent_exhaust(self, X=0, Y=60):
        self.value_rotation_vent_exhaust = StringVar()
        self.value_rotation_vent_exhaust.set(self.solution[self.count().__next__()])
        self.entry_rotation_vent_exhaust = ttk.Entry(self.lframe_vent_exhasut,textvariable=self.value_rotation_vent_exhaust).grid(column=X, row=Y, padx=10)
        self.lba_vent_exhaust(X, Y + 10, txt="Obroty [1/min]")

    def voltage_vent_exhaust(self, X=0, Y=80):
        self.value_voltage_vent_exhaust = StringVar()
        self.value_voltage_vent_exhaust.set(self.solution[self.count().__next__()])
        self.entry_voltage_vent_exhaust = ttk.Entry(self.lframe_vent_exhasut,textvariable=self.value_voltage_vent_exhaust).grid(column=X,row=Y, padx=10)
        self.lba_vent_exhaust(X, Y + 10, txt="Napięcie [V]")

    def frequency_vent_exhaust(self, X=0, Y=100):
        self.value_frequency_vent_exhaust = StringVar()
        self.value_frequency_vent_exhaust.set(self.solution[self.count().__next__()])
        self.entry_frequency_vent_exhaust = ttk.Entry(self.lframe_vent_exhasut, textvariable=self.value_frequency_vent_exhaust).grid(column=X, row=Y,padx=10)
        self.lba_vent_exhaust(X, Y + 10, txt="Częstotliwość [Hz]")

    def vent_exhaust_frame(self):
        self.lframe_vent_exhasut = ttk.LabelFrame(tab_3, text="sekcja wentylatora - Wywiew",)
        self.lframe_vent_exhasut.pack()
        self.type_vent_exhaust()
        self.power_vent_exhaust()
        self.current_vent_exhaust()
        self.rotation_vent_exhaust()
        self.voltage_vent_exhaust()
        self.frequency_vent_exhaust()

##################################################################################################################

    def lba_heater(self, X, Y, txt):
        return ttk.Label(self.lframe_heater, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)

    def heater_symbol(self, X=0, Y=0):
        self.value_heater_symbol = StringVar()
        self.value_heater_symbol.set(self.solution[self.count().__next__()])
        self.entry_heater_symbol = ttk.Entry(self.lframe_heater, textvariable=self.value_heater_symbol).grid(column=X,
                                                                                                             row=Y)
        self.lba_heater(X, Y, txt="Symbol")

    def heater_water_01(self, X=0, Y=3):

        self.lba_heater(X, Y - 1, txt="I woda")

        #
        self.value_heater_water_01_in = StringVar()
        self.value_heater_water_01_in.set(self.solution[self.count().__next__()])
        self.entry_heater_01_water_in = ttk.Entry(self.lframe_heater, textvariable=self.value_heater_water_01_in).grid(
            column=X, row=Y + 1, padx=10)
        self.lba_heater(X, Y + 1, txt="Zasilanie czynnika [°C]")

        #

        self.value_heater_01_water_out = StringVar()
        self.value_heater_01_water_out.set(self.solution[self.count().__next__()])
        self.entry_heater_water_electric_power = ttk.Entry(self.lframe_heater,textvariable=self.value_heater_01_water_out).grid(column=X,row=Y + 3,padx=10)
        self.lba_heater(X, Y + 3, txt="Powrót czynnika [°C]")

        self.value_heater_water_01_power = StringVar()
        self.value_heater_water_01_power.set(self.solution[self.count().__next__()])
        self.entry_heater_water_01_power = ttk.Entry(self.lframe_heater,textvariable=self.value_heater_water_01_power).grid(column=X, row=Y + 6,padx=10)
        self.lba_heater(X, Y + 6, txt="Moc [kW]")

        #
        self.value_heater_water_01_pressure_loss = StringVar()
        self.value_heater_water_01_pressure_loss.set(self.solution[self.count().__next__()])
        self.entry_heater_water_01_power = ttk.Entry(self.lframe_heater,textvariable=self.value_heater_water_01_pressure_loss).grid(column=X, row=Y + 9, padx=10)
        self.lba_heater(X, Y + 9, txt="Spadek ciśnienia [kPa]")

    def heater_water_02(self, X=20, Y=3):

        self.value_heater_02_water_in = StringVar()
        self.value_heater_02_water_in.set(self.solution[self.count().__next__()])
        self.lba_heater(X, Y - 1, txt="II")
        self.entry_heater_02_water_in = ttk.Entry(self.lframe_heater, textvariable=self.value_heater_02_water_in).grid(column=X, row=Y + 1, padx=10, sticky=W)
        self.lba_heater(X, Y + 1, txt="Temp. zasilanie czynnika [°C]")

        #

        self.value_heater_02_water_out = StringVar()
        self.value_heater_02_water_out.set(self.solution[self.count().__next__()])
        self.entry_heater_02_water_out = ttk.Entry(self.lframe_heater, textvariable=self.value_heater_02_water_out).grid(column=X, row=Y + 3, padx=10,sticky=W)
        self.lba_heater(X, Y + 3, txt="Temp. powrotu czynnika [°C]")
        #

        self.value_heater_water_02_power = StringVar()
        self.value_heater_water_02_power.set(self.solution[self.count().__next__()])
        self.entry_heater_water_02_power = ttk.Entry(self.lframe_heater,textvariable=self.value_heater_water_02_power).grid(column=X, row=Y + 6,  padx=10, sticky=W)
        self.lba_heater(X, Y + 6, txt="Moc [kW]")

        #

        self.value_heater_water_02_pressure_loss = StringVar()
        self.value_heater_water_02_pressure_loss.set(self.solution[self.count().__next__()])
        self.entry_heater_water_02_pressure_loss = ttk.Entry(self.lframe_heater, textvariable=self.value_heater_water_02_pressure_loss).grid( column=X, row=Y + 9, padx=10, sticky=W)
        self.lba_heater(X, Y + 9, txt="Spadek ciśnienia [kPa]")

    def heater_electric(self, X=30, Y=3):

        self.value_heater_electric_power_winter = StringVar()
        self.value_heater_electric_power_winter.set(self.solution[self.count().__next__()])
        self.entry_heater_electric_power_winter = ttk.Entry(self.lframe_heater, textvariable=self.value_heater_electric_power_winter).grid( column=X, row=Y + 1, padx=10, sticky=W)
        self.lba_heater(X, Y - 1, txt="Elektryczna")
        self.lba_heater(X, Y + 1, txt="Moc zima [kW]")

        #

        self.value_heater_02_water_power = StringVar()
        self.value_heater_02_water_power.set(())
        self.entry_heater_water_electric_power = ttk.Entry(self.lframe_heater,textvariable=self.value_heater_02_water_power).grid(column=X,    row=Y + 3,  padx=10,sticky=W)
        self.lba_heater(X, Y + 3, txt="Moc znamionowa [kW]")
        #

        self.value_heater_electric_voltage = StringVar()
        self.value_heater_electric_voltage.set(self.solution[self.count().__next__()])
        self.entry_heater_electric_voltage = ttk.Entry(self.lframe_heater, textvariable=self.value_heater_electric_voltage).grid(column=X,    row=Y + 6, padx=10, sticky=W)
        self.lba_heater(X, Y + 6, txt="Napięcie zasilania [V]")

    def heater_frame(self):
        self.lframe_heater = ttk.LabelFrame(tab_4, text="Nagrzewnice")
        self.lframe_heater.pack()
        self.heater_symbol()
        self.heater_water_01()
        self.heater_water_02()
        self.heater_electric()

    #######################################################################################################################

    def lba_cooler(self, X, Y, txt):
        return ttk.Label(self.lframe_cooler, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)

    def cooler_symbol(self, X=0, Y=0):
        self.value_cooler_symbol = StringVar()
        self.value_cooler_symbol.set(self.solution[self.count().__next__()])
        self.entry_cooler_symbol = ttk.Entry(self.lframe_cooler, textvariable=self.value_cooler_symbol).grid(column=X,row=Y, padx=10, sticky=W)
        self.lba_cooler(X, Y, "Symbol")

    def cooler_water(self, X=0, Y=3):

        self.value_cooler_water_in = StringVar()
        self.value_cooler_water_in.set(self.solution[self.count().__next__()])
        self.entry_cooler_water_in = ttk.Entry(self.lframe_cooler, textvariable=self.value_cooler_water_in).grid(
            column=X, row=Y, padx=10, sticky=W)
        self.lba_cooler(X, Y - 2, "Wodna")
        self.lba_cooler(X, Y + 1, "Temp. zasil. czynnika [°C]")

        self.value_cooler_water_out = StringVar()
        self.value_cooler_water_out.set(self.solution[self.count().__next__()])
        self.entry_cooler_water_out = ttk.Entry(self.lframe_cooler, textvariable=self.value_cooler_water_out).grid(column=X, row=Y + 3, padx=10, sticky=W)
        self.lba_cooler(X, Y + 3, "Temp. powr. czynnika [°C]")

        #
        self.value_cooler_water_power = StringVar()
        self.value_cooler_water_power.set(self.solution[self.count().__next__()])
        self.entry_cooler_water_power = ttk.Entry(self.lframe_cooler, textvariable=self.value_cooler_water_power).grid(column=X, row=Y + 6, padx=10, sticky=W)
        self.lba_cooler(X, Y + 6, "Moc lato [kW]")

        #

        self.value_cooler_water_pressure_loss = StringVar()
        self.value_cooler_water_pressure_loss.set(self.solution[self.count().__next__()])
        self.entry_pressure_loss = ttk.Entry(self.lframe_cooler,textvariable=self.value_cooler_water_pressure_loss).grid(column=X,row=Y + 9,padx=10, sticky=W)
        self.lba_cooler(X, Y + 9, " Opór hydrauliczny [kPa]")
        #

    def cooler_freon(self, X=30, Y=3):

        self.value_cooler_freon_refrig = StringVar()
        self.value_cooler_freon_refrig.set(self.solution[self.count().__next__()])
        self.entry_cooler_freon_refrig = ttk.Entry(self.lframe_cooler,textvariable=self.value_cooler_freon_refrig).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_cooler(X, Y - 2, "Freonowa")
        self.lba_cooler(X, Y + 1, "Rodzaj czynnika")

        #
        self.value_cooler_freon_power = StringVar()
        self.value_cooler_freon_power.set(self.solution[self.count().__next__()])
        self.entry_cooler_freon_refrig = ttk.Entry(self.lframe_cooler, textvariable=self.value_cooler_freon_power).grid(column=X, row=Y + 3, padx=10, sticky=W)
        self.lba_cooler(X, Y + 3, "Moc chłodnicy - lato [kW]")
        #
        self.value_cooler_freon_pressure_loss = StringVar()
        self.value_cooler_freon_pressure_loss.set(self.solution[self.count().__next__()])
        self.entry_cooler_freon_pressure_loss = ttk.Entry(self.lframe_cooler,textvariable=self.value_cooler_freon_pressure_loss).grid(
            column=X, row=Y + 6, padx=10, sticky=W)
        self.lba_cooler(X, Y + 6, "Opór hydrauliczny [kPa]")

    def cooler_frame(self):
        self.lframe_cooler = ttk.LabelFrame(tab_5, text="Chłodnica")
        self.lframe_cooler.pack()
        self.cooler_symbol()
        self.cooler_water()
        self.cooler_freon()

############################################################################################################################
    def lba_pre_filter_01_supply(self, X, Y, txt):
        return ttk.Label(self.lframe_pre_filter_01_supply, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10,sticky=W)

    def symbol_pre_filter_01_supply(self, X=0, Y=0):
        self.value_symbol_pre_filter_01_supply = StringVar()
        self.value_symbol_pre_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_pre_filter_01_supply = ttk.Entry(self.lframe_pre_filter_01_supply, textvariable=self.value_symbol_pre_filter_01_supply).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_01_supply(X, Y + 10, txt="Symbol")

    def class_pre_filter_01_supply(self, X=10, Y=0):
        self.value_class_pre_filter_01_supply = StringVar()
        self.value_class_pre_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_class_pre_filter_01_supply = ttk.Entry(self.lframe_pre_filter_01_supply, textvariable=self.value_class_pre_filter_01_supply).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_01_supply(X, Y + 10, txt="Klasa")

    def size_pre_filter_01_supply(self, X=20, Y=0):
        self.value_size_pre_filter_01_supply = StringVar()
        self.value_size_pre_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_size_pre_filter_01_supply = ttk.Entry(self.lframe_pre_filter_01_supply, textvariable=self.value_size_pre_filter_01_supply).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_01_supply(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_pre_filter_01_supply(self, X=30, Y=0):
        self.value_quantity_pre_filter_01_supply = StringVar()
        self.value_quantity_pre_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_quantity_pre_filter_01_supply = ttk.Entry(self.lframe_pre_filter_01_supply, textvariable=self.value_quantity_pre_filter_01_supply).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_01_supply(X, Y + 10, txt="Ilość [szt]")

    def pre_filter_supply_01_frame(self):
        self.lframe_pre_filter_01_supply = ttk.LabelFrame(tab_6, text="Filtr wstępny A")
        self.lframe_pre_filter_01_supply.pack()
        self.symbol_pre_filter_01_supply()
        self.class_pre_filter_01_supply()
        self.size_pre_filter_01_supply()
        self.quantity_pre_filter_01_supply()
#######################################################################################################################

    def lba_pre_filter_02_supply(self, X, Y, txt):
        return ttk.Label(self.lframe_pre_filter_02_supply, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10,
                                                                          sticky=W)

    def symbol_pre_filter_02_supply(self, X=0, Y=0):
        self.value_symbol_pre_filter_02_supply = StringVar()
        self.value_symbol_pre_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_pre_filter_02_supply = ttk.Entry(self.lframe_pre_filter_02_supply,textvariable=self.value_symbol_pre_filter_02_supply).grid(column=X,row=Y,padx=5)
        self.lba_pre_filter_02_supply(X, Y + 10, txt="Symbol")

    def class_pre_filter_02_supply(self, X=10, Y=0):
        self.value_class_pre_filter_02_supply = StringVar()
        self.value_class_pre_filter_02_supply.set(self.solution[self.count().__next__()])

        self.entry_class_pre_filter_02_supply = ttk.Entry(self.lframe_pre_filter_02_supply,textvariable=self.value_class_pre_filter_02_supply).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_02_supply(X, Y + 10, txt="Klasa")

    def size_pre_filter_02_supply(self, X=20, Y=0):
        self.value_size_pre_filter_02_supply = StringVar()
        self.value_size_pre_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_size_pre_filter_02_supply = ttk.Entry(self.lframe_pre_filter_02_supply,textvariable=self.value_size_pre_filter_02_supply).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_02_supply(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_pre_filter_02_supply(self, X=30, Y=0):
        self.value_quantity_pre_filter_02_supply = StringVar()
        self.value_quantity_pre_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_quantity_pre_filter_02_supply = ttk.Entry(self.lframe_pre_filter_02_supply,textvariable=self.value_quantity_pre_filter_02_supply).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_02_supply(X, Y + 10, txt="Ilość [szt]")

    def pre_filter_supply_02_frame(self):

        self.lframe_pre_filter_02_supply = ttk.LabelFrame(tab_6, text="Filtr wstępny B")
        self.lframe_pre_filter_02_supply.pack()
        self.symbol_pre_filter_02_supply()
        self.class_pre_filter_02_supply()
        self.size_pre_filter_02_supply()
        self.quantity_pre_filter_02_supply()



#######################################################################################################################

    def lba_second_filter_01_supply(self, X, Y, txt):
        return ttk.Label(self.lframe_second_filter_01_supply, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10,sticky=W)

    def symbol_second_filter_01_supply(self, X=0, Y=0):
        self.value_symbol_second_filter_01_supply = StringVar()
        self.value_symbol_second_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_second_filter_01_supply = ttk.Entry(self.lframe_second_filter_01_supply,textvariable=self.value_symbol_second_filter_01_supply).grid(column=X,row=Y,padx=5)
        self.lba_second_filter_01_supply(X, Y + 10, txt="Symbol")

    def class_second_filter_01_supply(self, X=10, Y=0):
        self.value_class_second_filter_01_supply = StringVar()
        self.value_class_second_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_class_second_filter_01_supply = ttk.Entry(self.lframe_second_filter_01_supply,textvariable=self.value_class_second_filter_01_supply).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_01_supply(X, Y + 10, txt="Klasa")

    def size_second_filter_01_supply(self, X=20, Y=0):
        self.value_size_second_filter_01_supply = StringVar()
        self.value_size_second_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_size_second_filter_01_supply = ttk.Entry(self.lframe_second_filter_01_supply,textvariable=self.value_size_second_filter_01_supply).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_01_supply(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_second_filter_01_supply(self, X=30, Y=0):
        self.value_quantity_second_filter_01_supply = StringVar()
        self.value_quantity_second_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_quantity_second_filter_01_supply = ttk.Entry(self.lframe_second_filter_01_supply,textvariable=self.value_quantity_second_filter_01_supply).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_01_supply(X, Y + 10, txt="Ilość [szt]")

    def second_filter_supply_01_frame(self):

        self.lframe_second_filter_01_supply = ttk.LabelFrame(tab_6, text="Filtr II stopnia A")
        self.lframe_second_filter_01_supply.pack()
        self.symbol_second_filter_01_supply()
        self.class_second_filter_01_supply()
        self.size_second_filter_01_supply()
        self.quantity_second_filter_01_supply()


######################################################################################################################\



    def lba_second_filter_02_supply(self, X, Y, txt):
        return ttk.Label(self.lframe_second_filter_02_supply, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10,sticky=W)

    def symbol_second_filter_02_supply(self, X=0, Y=0):
        self.value_symbol_second_filter_02_supply = StringVar()
        self.value_symbol_second_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_second_filter_02_supply = ttk.Entry(self.lframe_second_filter_02_supply,textvariable=self.value_symbol_second_filter_02_supply).grid(column=X,row=Y,padx=5)
        self.lba_second_filter_02_supply(X, Y + 10, txt="Symbol")

    def class_second_filter_02_supply(self, X=10, Y=0):
        self.value_class_second_filter_02_supply = StringVar()
        self.value_class_second_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_class_second_filter_02_supply = ttk.Entry(self.lframe_second_filter_02_supply,textvariable=self.value_class_second_filter_02_supply).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_02_supply(X, Y + 10, txt="Klasa")

    def size_second_filter_02_supply(self, X=20, Y=0):
        self.value_size_second_filter_02_supply = StringVar()
        self.value_size_second_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_size_second_filter_02_supply = ttk.Entry(self.lframe_second_filter_02_supply,textvariable=self.value_size_second_filter_02_supply).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_02_supply(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_second_filter_02_supply(self, X=30, Y=0):
        self.value_quantity_second_filter_02_supply = StringVar()
        self.value_quantity_second_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_quantity_second_filter_02_supply = ttk.Entry(self.lframe_second_filter_02_supply,textvariable=self.value_quantity_second_filter_02_supply).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_02_supply(X, Y + 10, txt="Ilość [szt]")

    def second_filter_supply_02_frame(self):

        self.lframe_second_filter_02_supply = ttk.LabelFrame(tab_6, text="Filtr II stopnia B")
        self.lframe_second_filter_02_supply.pack()
        self.symbol_second_filter_02_supply()
        self.class_second_filter_02_supply()
        self.size_second_filter_02_supply()
        self.quantity_second_filter_02_supply()

#######################################################################################################################

    def lba_third_filter_01_supply(self, X, Y, txt):
        return ttk.Label(self.lframe_third_filter_01_supply, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10,sticky=W)

    def symbol_third_filter_01_supply(self, X=0, Y=0):
        self.value_symbol_third_filter_01_supply = StringVar()
        self.value_symbol_third_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_third_filter_01_supply = ttk.Entry(self.lframe_third_filter_01_supply,textvariable=self.value_symbol_third_filter_01_supply).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_01_supply(X, Y + 10, txt="Symbol")

    def class_third_filter_01_supply(self, X=10, Y=0):
        self.value_class_third_filter_01_supply = StringVar()
        self.value_class_third_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_class_third_filter_01_supply = ttk.Entry(self.lframe_third_filter_01_supply,textvariable=self.value_class_third_filter_01_supply).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_01_supply(X, Y + 10, txt="Klasa")

    def size_third_filter_01_supply(self, X=20, Y=0):
        self.value_size_third_filter_01_supply = StringVar()
        self.value_size_third_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_size_third_filter_01_supply = ttk.Entry(self.lframe_third_filter_01_supply,textvariable=self.value_size_third_filter_01_supply).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_01_supply(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_third_filter_01_supply(self, X=30, Y=0):
        self.value_quantity_third_filter_01_supply = StringVar()
        self.value_quantity_third_filter_01_supply.set(self.solution[self.count().__next__()])
        self.entry_quantity_third_filter_01_supply = ttk.Entry(self.lframe_third_filter_01_supply,textvariable=self.value_quantity_third_filter_01_supply).grid(
            column=X, row=Y, padx=5)
        self.lba_third_filter_01_supply(X, Y + 10, txt="Ilość [szt]")

    def third_filter_supply_01_frame(self):
        self.lframe_third_filter_01_supply = ttk.LabelFrame(tab_6, text="Filtr III stopnia A")
        self.lframe_third_filter_01_supply.pack()
        self.symbol_third_filter_01_supply()
        self.class_third_filter_01_supply()
        self.size_third_filter_01_supply()
        self.quantity_third_filter_01_supply()

    ########################################################################################################################

    def lba_third_filter_02_supply(self, X, Y, txt):
        return ttk.Label(self.lframe_third_filter_02_supply, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)

    def symbol_third_filter_02_supply(self, X=0, Y=0):
        self.value_symbol_third_filter_02_supply = StringVar()
        self.value_symbol_third_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_third_filter_02_supply = ttk.Entry(self.lframe_third_filter_02_supply,textvariable=self.value_symbol_third_filter_02_supply).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_02_supply(X, Y + 10, txt="Symbol")

    def class_third_filter_02_supply(self, X=10, Y=0):
        self.value_class_third_filter_02_supply = StringVar()
        self.value_class_third_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_class_third_filter_02_supply = ttk.Entry(self.lframe_third_filter_02_supply,textvariable=self.value_class_third_filter_02_supply).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_02_supply(X, Y + 10, txt="Klasa")

    def size_third_filter_02_supply(self, X=20, Y=0):
        self.value_size_third_filter_02_supply = StringVar()
        self.value_size_third_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_size_third_filter_02_supply = ttk.Entry(self.lframe_third_filter_02_supply,textvariable=self.value_size_third_filter_02_supply).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_02_supply(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_third_filter_02_supply(self, X=30, Y=0):
        self.value_quantity_third_filter_02_supply = StringVar()
        self.value_quantity_third_filter_02_supply.set(self.solution[self.count().__next__()])
        self.entry_quantity_third_filter_02_supply = ttk.Entry(self.lframe_third_filter_02_supply,textvariable=self.value_quantity_third_filter_02_supply).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_02_supply(X, Y + 10, txt="Ilość [szt]")

    def third_filter_supply_02_frame(self):
        self.lframe_third_filter_02_supply = ttk.LabelFrame(tab_6, text="Filtr III stopnia B")
        self.lframe_third_filter_02_supply.pack()
        self.symbol_third_filter_02_supply()
        self.class_third_filter_02_supply()
        self.size_third_filter_02_supply()
        self.quantity_third_filter_02_supply()

    #######################################################################################################################



    def lba_pre_filter_01_exhaust(self, X, Y, txt):
        return ttk.Label(self.lframe_pre_filter_01_exhaust, text=txt).grid(column=X, row=Y + 1, pady=(1, 10),padx=10, sticky=W)

    def symbol_pre_filter_01_exhaust(self, X=0, Y=0):
        self.value_symbol_pre_filter_01_exhaust = StringVar()
        self.value_symbol_pre_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_pre_filter_01_exhaust = ttk.Entry(self.lframe_pre_filter_01_exhaust,textvariable=self.value_symbol_pre_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_01_exhaust(X, Y + 10, txt="Symbol")

    def class_pre_filter_01_exhaust(self, X=10, Y=0):
        self.value_class_pre_filter_01_exhaust = StringVar()
        self.value_class_pre_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_class_pre_filter_01_exhaust = ttk.Entry(self.lframe_pre_filter_01_exhaust,textvariable=self.value_class_pre_filter_01_exhaust).grid( column=X, row=Y, padx=5)
        self.lba_pre_filter_01_exhaust(X, Y + 10, txt="Klasa")

    def size_pre_filter_01_exhaust(self, X=20, Y=0):
        self.value_size_pre_filter_01_exhaust = StringVar()
        self.value_size_pre_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_size_pre_filter_01_exhaust = ttk.Entry(self.lframe_pre_filter_01_exhaust,textvariable=self.value_size_pre_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_01_exhaust(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_pre_filter_01_exhaust(self, X=30, Y=0):
        self.value_quantity_pre_filter_01_exhaust = StringVar()
        self.value_quantity_pre_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_quantity_pre_filter_01_exhaust = ttk.Entry(self.lframe_pre_filter_01_exhaust,textvariable=self.value_quantity_pre_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_01_exhaust(X, Y + 10, txt="Ilość [szt]")

    def pre_filter_exhaust_01_frame(self):
        self.lframe_pre_filter_01_exhaust = ttk.LabelFrame(tab_7, text="Filtr wstępny A")
        self.lframe_pre_filter_01_exhaust.pack()
        self.symbol_pre_filter_01_exhaust()
        self.class_pre_filter_01_exhaust()
        self.size_pre_filter_01_exhaust()
        self.quantity_pre_filter_01_exhaust()

    #######################################################################################################################

    def lba_pre_filter_02_exhaust(self, X, Y, txt):
        return ttk.Label(self.lframe_pre_filter_02_exhaust, text=txt).grid(column=X, row=Y + 1, pady=(1, 10),padx=10,sticky=W)

    def symbol_pre_filter_02_exhaust(self, X=0, Y=0):
        self.value_symbol_pre_filter_02_exhaust = StringVar()
        self.value_symbol_pre_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_pre_filter_02_exhaust = ttk.Entry(self.lframe_pre_filter_02_exhaust,textvariable=self.value_symbol_pre_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_02_exhaust(X, Y + 10, txt="Symbol")

    def class_pre_filter_02_exhaust(self, X=10, Y=0):
        self.value_class_pre_filter_02_exhaust = StringVar()
        self.value_class_pre_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_class_pre_filter_02_exhaust = ttk.Entry(self.lframe_pre_filter_02_exhaust,textvariable=self.value_class_pre_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_02_exhaust(X, Y + 10, txt="Klasa")

    def size_pre_filter_02_exhaust(self, X=20, Y=0):
        self.value_size_pre_filter_02_exhaust = StringVar()
        self.value_size_pre_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_size_pre_filter_02_exhaust = ttk.Entry(self.lframe_pre_filter_02_exhaust,textvariable=self.value_size_pre_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_02_exhaust(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_pre_filter_02_exhaust(self, X=30, Y=0):
        self.value_quantity_pre_filter_02_exhaust = StringVar()
        self.value_quantity_pre_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_quantity_pre_filter_02_exhaust = ttk.Entry(self.lframe_pre_filter_02_exhaust,textvariable=self.value_quantity_pre_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_pre_filter_02_exhaust(X, Y + 10, txt="Ilość [szt]")

    def pre_filter_exhaust_02_frame(self):
        self.lframe_pre_filter_02_exhaust = ttk.LabelFrame(tab_7, text="Filtr wstępny B")
        self.lframe_pre_filter_02_exhaust.pack()
        self.symbol_pre_filter_02_exhaust()
        self.class_pre_filter_02_exhaust()
        self.size_pre_filter_02_exhaust()
        self.quantity_pre_filter_02_exhaust()


    #######################################################################################################################

    def lba_second_filter_01_exhaust(self, X, Y, txt):
        return ttk.Label(self.lframe_second_filter_01_exhaust, text=txt).grid(column=X, row=Y + 1, pady=(1, 10),padx=10, sticky=W)

    def symbol_second_filter_01_exhaust(self, X=0, Y=0):
        self.value_symbol_second_filter_01_exhaust = StringVar()
        self.value_symbol_second_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_second_filter_01_exhaust = ttk.Entry(self.lframe_second_filter_01_exhaust,textvariable=self.value_symbol_second_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_01_exhaust(X, Y + 10, txt="Symbol")

    def class_second_filter_01_exhaust(self, X=10, Y=0):
        self.value_class_second_filter_01_exhaust = StringVar()
        self.value_class_second_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_class_second_filter_01_exhaust = ttk.Entry(self.lframe_second_filter_01_exhaust,textvariable=self.value_class_second_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_01_exhaust(X, Y + 10, txt="Klasa")

    def size_second_filter_01_exhaust(self, X=20, Y=0):
        self.value_size_second_filter_01_exhaust = StringVar()
        self.value_size_second_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_size_second_filter_01_exhaust = ttk.Entry(self.lframe_second_filter_01_exhaust,textvariable=self.value_size_second_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_01_exhaust(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_second_filter_01_exhaust(self, X=30, Y=0):
        self.value_quantity_second_filter_01_exhaust = StringVar()
        self.value_quantity_second_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_quantity_second_filter_01_exhaust = ttk.Entry(self.lframe_second_filter_01_exhaust,textvariable=self.value_quantity_second_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_01_exhaust(X, Y + 10, txt="Ilość [szt]")

    def second_filter_exhaust_01_frame(self):
        self.lframe_second_filter_01_exhaust = ttk.LabelFrame(tab_7, text="Filtr II stopnia A")
        self.lframe_second_filter_01_exhaust.pack()
        self.symbol_second_filter_01_exhaust()
        self.class_second_filter_01_exhaust()
        self.size_second_filter_01_exhaust()
        self.quantity_second_filter_01_exhaust()

    ######################################################################################################################\

    def lba_second_filter_02_exhaust(self, X, Y, txt):
        return ttk.Label(self.lframe_second_filter_02_exhaust, text=txt).grid(column=X, row=Y + 1, pady=(1, 10),
                                                                              padx=10, sticky=W)

    def symbol_second_filter_02_exhaust(self, X=0, Y=0):
        self.value_symbol_second_filter_02_exhaust = StringVar()
        self.value_symbol_second_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_second_filter_02_exhaust = ttk.Entry(self.lframe_second_filter_02_exhaust,textvariable=self.value_symbol_second_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_02_exhaust(X, Y + 10, txt="Symbol")

    def class_second_filter_02_exhaust(self, X=10, Y=0):
        self.value_class_second_filter_02_exhaust = StringVar()
        self.value_class_second_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_class_second_filter_02_exhaust = ttk.Entry(self.lframe_second_filter_02_exhaust,textvariable=self.value_class_second_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_02_exhaust(X, Y + 10, txt="Klasa")

    def size_second_filter_02_exhaust(self, X=20, Y=0):
        self.value_size_second_filter_02_exhaust = StringVar()
        self.value_size_second_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_size_second_filter_02_exhaust = ttk.Entry(self.lframe_second_filter_02_exhaust,textvariable=self.value_size_second_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_02_exhaust(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_second_filter_02_exhaust(self, X=30, Y=0):
        self.value_quantity_second_filter_02_exhaust = StringVar()
        self.value_quantity_second_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_quantity_second_filter_02_exhaust = ttk.Entry(self.lframe_second_filter_02_exhaust,textvariable=self.value_quantity_second_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_second_filter_02_exhaust(X, Y + 10, txt="Ilość [szt]")

    def second_filter_exhaust_02_frame(self):
        self.lframe_second_filter_02_exhaust = ttk.LabelFrame(tab_7, text="Filtr II stopnia B")
        self.lframe_second_filter_02_exhaust.pack()
        self.symbol_second_filter_02_exhaust()
        self.class_second_filter_02_exhaust()
        self.size_second_filter_02_exhaust()
        self.quantity_second_filter_02_exhaust()

    #######################################################################################################################

    def lba_third_filter_01_exhaust(self, X, Y, txt):
        return ttk.Label(self.lframe_third_filter_01_exhaust, text=txt).grid(column=X, row=Y + 1, pady=(1, 10),padx=10,sticky=W)

    def symbol_third_filter_01_exhaust(self, X=0, Y=0):
        self.value_symbol_third_filter_01_exhaust = StringVar()
        self.value_symbol_third_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_third_filter_01_exhaust = ttk.Entry(self.lframe_third_filter_01_exhaust,textvariable=self.value_symbol_third_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_01_exhaust(X, Y + 10, txt="Symbol")

    def class_third_filter_01_exhaust(self, X=10, Y=0):
        self.value_class_third_filter_01_exhaust = StringVar()
        self.value_class_third_filter_01_exhaust.set(self.solution[self.count().__next__()])

        self.entry_class_third_filter_01_exhaust = ttk.Entry(self.lframe_third_filter_01_exhaust,textvariable=self.value_class_third_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_01_exhaust(X, Y + 10, txt="Klasa")

    def size_third_filter_01_exhaust(self, X=20, Y=0):
        self.value_size_third_filter_01_exhaust = StringVar()
        self.value_size_third_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_size_third_filter_01_exhaust = ttk.Entry(self.lframe_third_filter_01_exhaust,textvariable=self.value_size_third_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_01_exhaust(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_third_filter_01_exhaust(self, X=30, Y=0):
        self.value_quantity_third_filter_01_exhaust = StringVar()
        self.value_quantity_third_filter_01_exhaust.set(self.solution[self.count().__next__()])
        self.entry_quantity_third_filter_01_exhaust = ttk.Entry(self.lframe_third_filter_01_exhaust,textvariable=self.value_quantity_third_filter_01_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_01_exhaust(X, Y + 10, txt="Ilość [szt]")

    def third_filter_exhaust_01_frame(self):
        self.lframe_third_filter_01_exhaust = ttk.LabelFrame(tab_7, text="Filtr III stopnia A")
        self.lframe_third_filter_01_exhaust.pack()
        self.symbol_third_filter_01_exhaust()
        self.class_third_filter_01_exhaust()
        self.size_third_filter_01_exhaust()
        self.quantity_third_filter_01_exhaust()

    ########################################################################################################################

    def lba_third_filter_02_exhaust(self, X, Y, txt):
        return ttk.Label(self.lframe_third_filter_02_exhaust, text=txt).grid(column=X, row=Y + 1, pady=(1, 10),padx=10,sticky=W)

    def symbol_third_filter_02_exhaust(self, X=0, Y=0):
        self.value_symbol_third_filter_02_exhaust = StringVar()
        self.value_symbol_third_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_third_filter_02_exhaust = ttk.Entry(self.lframe_third_filter_02_exhaust,textvariable=self.value_symbol_third_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_02_exhaust(X, Y + 10, txt="Symbol")

    def class_third_filter_02_exhaust(self, X=10, Y=0):
        self.value_class_third_filter_02_exhaust = StringVar()
        self.value_class_third_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_class_third_filter_02_exhaust = ttk.Entry(self.lframe_third_filter_02_exhaust,textvariable=self.value_class_third_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_02_exhaust(X, Y + 10, txt="Klasa")

    def size_third_filter_02_exhaust(self, X=20, Y=0):
        self.value_size_third_filter_02_exhaust = StringVar()
        self.value_size_third_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_size_third_filter_02_exhaust = ttk.Entry(self.lframe_third_filter_02_exhaust,textvariable=self.value_size_third_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_02_exhaust(X, Y + 10, txt="Rozmiar [mm]")

    def quantity_third_filter_02_exhaust(self, X=30, Y=0):
        self.value_quantity_third_filter_02_exhaust = StringVar()
        self.value_quantity_third_filter_02_exhaust.set(self.solution[self.count().__next__()])
        self.entry_quantity_third_filter_02_exhaust = ttk.Entry(self.lframe_third_filter_02_exhaust,textvariable=self.value_quantity_third_filter_02_exhaust).grid(column=X, row=Y, padx=5)
        self.lba_third_filter_02_exhaust(X, Y + 10, txt="Ilość [szt]")

    def third_filter_exhaust_02_frame(self):
        self.lframe_third_filter_02_exhaust = ttk.LabelFrame(tab_7, text="Filtr III stopnia B")
        self.lframe_third_filter_02_exhaust.pack()
        self.symbol_third_filter_02_exhaust()
        self.class_third_filter_02_exhaust()
        self.size_third_filter_02_exhaust()
        self.quantity_third_filter_02_exhaust()



########################################################################################################################

    def lba_heat_recovery(self, X, Y, txt):
        return ttk.Label(self.lframe_counter , text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)

    def heat_recovery_symbol(self, X=0, Y=0):
        self.value_heat_recovery = StringVar()
        self.value_heat_recovery.set(self.solution[self.count().__next__()])
        self.entry_heat_recovery_symbol = ttk.Entry(self.lframe_counter, textvariable=self.value_heat_recovery).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_heat_recovery(X, Y, "Symbol")


    def counterflow_frame(self):
        self.lframe_counter = ttk.LabelFrame(tab_8, text="Symbol wymiennika ")
        self.lframe_counter.pack()
        self.heat_recovery_symbol()


#######################################################################################################################

    def lba_heat_rec(self, X, Y, txt):

        return ttk.Label(self.lframe_heat_rec, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)

    def glicol_symbol_motor_typ(self,X=0, Y=10):

        self.value_glicol_symbol_motor_typ=StringVar()
        self.value_glicol_symbol_motor_typ.set(self.solution[self.count().__next__()])

        self.entry_glicol_motor_typ = ttk.Entry(self.lframe_heat_rec, textvariable=self.value_glicol_symbol_motor_typ).grid(column=X, row=Y, padx=10, sticky=W)

        self.lba_heat_rec(X, Y, "Sym. pompy siln. odzysku")

    def glicol_symbol_motor_pwr(self, X=0, Y=30):

        self.value_glicol_motor_pwr = StringVar()
        self.value_glicol_motor_pwr.set(self.solution[self.count().__next__()])
        self.entry_glicol_motor_pwr = ttk.Entry(self.lframe_heat_rec, textvariable=self.value_glicol_motor_pwr).grid(column=X, row=Y, padx=10, sticky=W)

        self.lba_heat_rec(X, Y, "Moc sil. p-y glikolu [kW]")


    def glicol_symbol_motor_voltage(self, X=0, Y=60):
        self.value_glicol_motor_voltage = StringVar()
        self.value_glicol_motor_voltage.set(self.solution[self.count().__next__()])
        self.entry_glicol_motor_voltage = ttk.Entry(self.lframe_heat_rec, textvariable=self.value_glicol_motor_voltage).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_heat_rec(X, Y, "Napięcie zas. pompy [V]")

    def rotor_exchanger_symbol_motor_pwr(self, X=20, Y=30):
        self.value_rotor_exchanger_motor_pwr = StringVar()
        self.value_rotor_exchanger_motor_pwr.set(self.solution[self.count().__next__()])
        self.entry_rotor_exchanger_motor_pwr = ttk.Entry(self.lframe_heat_rec,textvariable=self.value_rotor_exchanger_motor_pwr).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_heat_rec(X, Y, "Moc sil. wym. obr. [kW]")


    def rotor_exchanger_symbol_motor_voltage(self, X=20, Y=60):
        self.value_rotor_exchanger_motor_voltage = StringVar()
        self.value_rotor_exchanger_motor_voltage.set(self.solution[self.count().__next__()])
        self.entry_rotor_exchanger_motor_voltage = ttk.Entry(self.lframe_heat_rec,textvariable=self.value_rotor_exchanger_motor_voltage).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_heat_rec(X, Y, "Napięcie zas. silnika wym .obr. [V]")




    def heat_rec_frame(self):
        self.lframe_heat_rec = ttk.LabelFrame(tab_8, text="Parametry")
        self.lframe_heat_rec.pack()
        self.glicol_symbol_motor_pwr()
        self.glicol_symbol_motor_voltage()
        self.rotor_exchanger_symbol_motor_pwr()
        self.rotor_exchanger_symbol_motor_voltage()
        self.glicol_symbol_motor_typ()




#########################################################################################################################

    def lba_humidifier(self, X, Y, txt):
        return ttk.Label(self.lframe_humidifier, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)



    def humidifier_typ(self, X=0, Y=10):
        self.value_humidifier_typ = StringVar()
        self.value_humidifier_typ.set(self.solution[self.count().__next__()])
        self.entry_humidifier_typ = ttk.Entry(self.lframe_humidifier, textvariable=self.value_humidifier_typ).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_humidifier(X, Y, "Symbol")


    def humidifier_outgo(self, X=0, Y=20):
        self.value_humidifier_outgo = StringVar()
        self.value_humidifier_outgo.set(self.solution[self.count().__next__()])
        self.entry_humidifier_outgo = ttk.Entry(self.lframe_humidifier, textvariable=self.value_humidifier_outgo).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_humidifier(X, Y, "Wydajność [kg/h]")

    def humidifier_pwr(self, X=0, Y=30):
        self.value_humidifier_pwr = StringVar()
        self.value_humidifier_pwr.set(self.solution[self.count().__next__()])
        self.entry_humidifier_pwr = ttk.Entry(self.lframe_humidifier, textvariable=self.value_humidifier_pwr).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_humidifier(X, Y, "Moc [kW]")

    def humidifier_voltage(self, X=0, Y=60):
        self.value_humidifier_voltage = StringVar()
        self.value_humidifier_voltage.set(self.solution[self.count().__next__()])
        self.entry_humidifier_voltage = ttk.Entry(self.lframe_humidifier,textvariable=self.value_humidifier_voltage).grid(column=X, row=Y,padx=10, sticky=W)
        self.lba_humidifier(X, Y, "Napięcie zasilania [V]")



    def humidifier_frame(self):
        self.lframe_humidifier = ttk.LabelFrame(tab_9, text="Nawilżacz")
        self.lframe_humidifier.pack(side = LEFT, expand = True, fill = X)
        self.humidifier_pwr()
        self.humidifier_voltage()
        self.humidifier_typ()
        self.humidifier_outgo()

###########################################################################################################################


    def lba_humidifier_pump(self, X, Y, txt):
        return ttk.Label(self.lframe_humidifier_pump, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)



    def humidifier_pump_typ(self, X=0, Y=10):
        self.value_humidifier_pump_typ = StringVar()
        self.value_humidifier_pump_typ.set(self.solution[self.count().__next__()])
        self.entry_humidifier_pump_typ = ttk.Entry(self.lframe_humidifier_pump, textvariable=self.value_humidifier_pump_typ).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_humidifier_pump(X, Y, "Symbol")


    def humidifier_pump_current(self, X=0, Y=20):
        self.value_humidifier_pump_current = StringVar()
        self.value_humidifier_pump_current.set(self.solution[self.count().__next__()])
        self.entry_humidifier_pump_current = ttk.Entry(self.lframe_humidifier_pump, textvariable=self.value_humidifier_pump_current).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_humidifier_pump(X, Y, "Prąd [A]]")

    def humidifier_pump_pwr(self, X=0, Y=30):
        self.value_humidifier_pump_pwr = StringVar()
        self.value_humidifier_pump_pwr.set(self.solution[self.count().__next__()])
        self.entry_humidifier_pump_pwr = ttk.Entry(self.lframe_humidifier_pump, textvariable=self.value_humidifier_pump_pwr).grid(column=X, row=Y, padx=10, sticky=W)
        self.lba_humidifier_pump(X, Y, "Moc [kW]")

    def humidifier_pump_voltage(self, X=0, Y=60):
        self.value_humidifier_pump_voltage = StringVar()
        self.value_humidifier_pump_voltage.set(self.solution[self.count().__next__()])
        self.entry_humidifier_pump_voltage = ttk.Entry(self.lframe_humidifier_pump,textvariable=self.value_humidifier_pump_voltage).grid(column=X, row=Y,padx=10, sticky=W)

        self.lba_humidifier_pump(X, Y, "Napięcie zasilania [V]")



    def humidifier_pump_frame(self):
        self.lframe_humidifier_pump = ttk.LabelFrame(tab_9, text="Pompa nawilżacza")
        self.lframe_humidifier_pump.pack(side = LEFT,expand= TRUE, fill = X)
        self.humidifier_pump_pwr()
        self.humidifier_pump_voltage()
        self.humidifier_pump_typ()
        self.humidifier_pump_current()


########################################################################################################################



    def lba_aggregat(self, X, Y, txt):
        return ttk.Label(self.lframe_aggregat, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)


    def type_aggregat(self, X=0, Y=0):
        self.value_aggregat_typ = StringVar()
        self.value_aggregat_typ.set(self.solution[self.count().__next__()])
        self.entry_aggregat = ttk.Entry(self.lframe_aggregat, textvariable=self.value_aggregat_typ).grid(column=X, row=Y, padx=10)
        self.lba_aggregat(X, Y + 10, txt="Symbol")


    def voltage_aggregat(self, X=0, Y=20):
        self.value_voltage_aggregat = StringVar()
        self.value_voltage_aggregat.set(self.solution[self.count().__next__()])
        self.entry_voltage_aggregat = ttk.Entry(self.lframe_aggregat, textvariable=self.value_voltage_aggregat).grid(column=X, row=Y, padx=10)
        self.lba_aggregat(X, Y + 10, txt="Napięcie zasilania[V]")


    def start_current_aggregat(self, X=0, Y=40):
        self.value_start_current_aggregat = StringVar()
        self.value_start_current_aggregat.set(self.solution[self.count().__next__()])
        self.entry_start_current_aggregat = ttk.Entry(self.lframe_aggregat, textvariable=self.value_start_current_aggregat).grid(column=X, row=Y, padx=10)
        self.lba_aggregat(X, Y + 10, txt="Prąd rozruchu[A]")

    def max_current_aggregat(self, X=0, Y=60):
        self.value_max_current_aggregat = StringVar()
        self.value_max_current_aggregat.set(self.solution[self.count().__next__()])
        self.entry_max_current_aggregat = ttk.Entry(self.lframe_aggregat, textvariable=self.value_max_current_aggregat).grid(column=X, row=Y, padx=10)
        self.lba_aggregat(X, Y + 10, txt="Max prąd [A]")


    def aggregat_frame(self):
        self.lframe_aggregat = ttk.LabelFrame(tab_9, text="Agregat chłodniczy")
        self.lframe_aggregat.pack(side = RIGHT, expand = True, fill = X)
        self.type_aggregat()
        self.voltage_aggregat()
        self.start_current_aggregat()
        self.max_current_aggregat()


########################################################################################################################
    def lba_mass(self, X, Y, txt):
        return ttk.Label(self.lframe_mass, text=txt).grid(column=X, row=Y + 1, pady=(1, 10), padx=10, sticky=W)

    def mass(self, X=0, Y=10):
        self.lba_mass(X, Y, "masa [kg]")
        self.value_mass = StringVar()
        self.value_mass.set(self.solution[self.count().__next__()])
        self.entry_mass = ttk.Entry(self.lframe_mass, textvariable=self.value_mass).grid(column=X, row=Y, padx=10, sticky=W)

    def mass_frame(self):
        self.lframe_mass = ttk.LabelFrame(tab_9, text="Masa")
        self.lframe_mass.pack(side = BOTTOM,fill=X ,expand = TRUE)
        self.mass()
#########################################################################################################################
    def group_various(self):
        self.lframe_various = ttk.LabelFrame(tab_9, text="różne")
        self.lframe_various.pack(side = TOP,fill=X,expand = FALSE )
        self.aggregat_frame()
        self.humidifier_frame()
        self.humidifier_pump_frame()

########################################################################################################################

    # def print(self):
    #
    #     all_attribute = (self.__dict__)
    #     target = re.compile(r'value', re.IGNORECASE)
    #     collect= list()
    #     for a in  all_attribute :
    #         if 'value'in a:
    #             collect.append(a)
    #
    #     print (collect)
    #     print (len(collect))


    def get_method_SV(self):

        self.export_project_no = self.value_project_no.get()
        self.export_order_no = self.value_order_no.get()
        self.export_se_num = self.value_se_num.get()
        self.export_model_symbol = self.value_model_symbol.get()
        self.export_system_symbol = self.value_system_symbol.get()
        self.export_supply_symbol = self.value_supply_symbol.get()
        self.export_output_supply = self.value_output_supply.get()
        self.export_pressure_supply = self.value_pressure_supply.get()
        self.export_vent_supply_symbol = self.value_vent_supply_symbol.get()
        self.export_power_supply = self.value_power_supply.get()
        self.export_current_supply = self.value_current_supply.get()
        self.export_rotation_supply = self.value_rotation_supply.get()
        self.export_voltage_supply = self.value_voltage_supply.get()
        self.export_frequency_supply = self.value_frequency_supply.get()
        self.export_exhaust_symbol = self.value_exhaust_symbol.get()
        self.export_output_exhaust = self.value_output_exhaust.get()
        self.export_pressure_exhaust = self.value_pressure_exhaust.get()
        self.export_vent_exhaust_symbol = self.value_vent_exhaust_symbol.get()
        self.export_power_vent_exhaust = self.value_power_vent_exhaust.get()
        self.export_current_vent_exhaust = self.value_current_vent_exhaust.get()
        self.export_rotation_vent_exhaust = self.value_rotation_vent_exhaust.get()
        self.export_voltage_vent_exhaust = self.value_voltage_vent_exhaust.get()
        self.export_frequency_vent_exhaust = self.value_frequency_vent_exhaust.get()
        self.export_heater_symbol = self.value_heater_symbol.get()
        self.export_heater_water_01_in = self.value_heater_water_01_in.get()
        self.export_heater_01_water_out = self.value_heater_01_water_out.get()
        self.export_heater_water_01_power = self.value_heater_water_01_power.get()
        self.export_heater_water_01_pressure_loss = self.value_heater_water_01_pressure_loss.get()
        self.export_heater_02_water_in = self.value_heater_02_water_in.get()
        self.export_heater_02_water_out = self.value_heater_02_water_out.get()
        self.export_heater_water_02_power = self.value_heater_water_02_power.get()
        self.export_heater_water_02_pressure_loss = self.value_heater_water_02_pressure_loss.get()
        self.export_heater_electric_power_winter = self.value_heater_electric_power_winter.get()
        self.export_heater_02_water_power = self.value_heater_02_water_power.get()
        self.export_heater_electric_voltage = self.value_heater_electric_voltage.get()
        self.export_cooler_symbol = self.value_cooler_symbol.get()
        self.export_cooler_water_in = self.value_cooler_water_in.get()
        self.export_cooler_water_out = self.value_cooler_water_out.get()
        self.export_cooler_water_power = self.value_cooler_water_power.get()
        self.export_cooler_water_pressure_loss = self.value_cooler_water_pressure_loss.get()
        self.export_cooler_freon_refrig = self.value_cooler_freon_refrig.get()
        self.export_cooler_freon_power = self.value_cooler_freon_power.get()
        self.export_cooler_freon_pressure_loss = self.value_cooler_freon_pressure_loss.get()
        self.export_symbol_pre_filter_01_supply = self.value_symbol_pre_filter_01_supply.get()
        self.export_class_pre_filter_01_supply = self.value_class_pre_filter_01_supply.get()
        self.export_size_pre_filter_01_supply = self.value_size_pre_filter_01_supply.get()
        self.export_quantity_pre_filter_01_supply = self.value_quantity_pre_filter_01_supply.get()
        self.export_symbol_pre_filter_02_supply = self.value_symbol_pre_filter_02_supply.get()
        self.export_class_pre_filter_02_supply = self.value_class_pre_filter_02_supply.get()
        self.export_size_pre_filter_02_supply = self.value_size_pre_filter_02_supply.get()
        self.export_quantity_pre_filter_02_supply = self.value_quantity_pre_filter_02_supply.get()
        self.export_symbol_second_filter_01_supply = self.value_symbol_second_filter_01_supply.get()
        self.export_class_second_filter_01_supply = self.value_class_second_filter_01_supply.get()
        self.export_size_second_filter_01_supply = self.value_size_second_filter_01_supply.get()
        self.export_quantity_second_filter_01_supply = self.value_quantity_second_filter_01_supply.get()
        self.export_symbol_second_filter_02_supply = self.value_symbol_second_filter_02_supply.get()
        self.export_class_second_filter_02_supply = self.value_class_second_filter_02_supply.get()
        self.export_size_second_filter_02_supply = self.value_size_second_filter_02_supply.get()
        self.export_quantity_second_filter_02_supply = self.value_quantity_second_filter_02_supply.get()
        self.export_symbol_third_filter_01_supply = self.value_symbol_third_filter_01_supply.get()
        self.export_class_third_filter_01_supply = self.value_class_third_filter_01_supply.get()
        self.export_size_third_filter_01_supply = self.value_size_third_filter_01_supply.get()
        self.export_quantity_third_filter_01_supply = self.value_quantity_third_filter_01_supply.get()
        self.export_symbol_third_filter_02_supply = self.value_symbol_third_filter_02_supply.get()
        self.export_class_third_filter_02_supply = self.value_class_third_filter_02_supply.get()
        self.export_size_third_filter_02_supply = self.value_size_third_filter_02_supply.get()
        self.export_quantity_third_filter_02_supply = self.value_quantity_third_filter_02_supply.get()
        self.export_symbol_pre_filter_01_exhaust = self.value_symbol_pre_filter_01_exhaust.get()
        self.export_class_pre_filter_01_exhaust = self.value_class_pre_filter_01_exhaust.get()
        self.export_size_pre_filter_01_exhaust = self.value_size_pre_filter_01_exhaust.get()
        self.export_quantity_pre_filter_01_exhaust = self.value_quantity_pre_filter_01_exhaust.get()
        self.export_symbol_pre_filter_02_exhaust = self.value_symbol_pre_filter_02_exhaust.get()
        self.export_class_pre_filter_02_exhaust = self.value_class_pre_filter_02_exhaust.get()
        self.export_size_pre_filter_02_exhaust = self.value_size_pre_filter_02_exhaust.get()
        self.export_quantity_pre_filter_02_exhaust = self.value_quantity_pre_filter_02_exhaust.get()
        self.export_symbol_second_filter_01_exhaust = self.value_symbol_second_filter_01_exhaust.get()
        self.export_class_second_filter_01_exhaust = self.value_class_second_filter_01_exhaust.get()
        self.export_size_second_filter_01_exhaust = self.value_size_second_filter_01_exhaust.get()
        self.export_quantity_second_filter_01_exhaust = self.value_quantity_second_filter_01_exhaust.get()
        self.export_symbol_second_filter_02_exhaust = self.value_symbol_second_filter_02_exhaust.get()
        self.export_class_second_filter_02_exhaust = self.value_class_second_filter_02_exhaust.get()
        self.export_size_second_filter_02_exhaust = self.value_size_second_filter_02_exhaust.get()
        self.export_quantity_second_filter_02_exhaust = self.value_quantity_second_filter_02_exhaust.get()
        self.export_symbol_third_filter_01_exhaust = self.value_symbol_third_filter_01_exhaust.get()
        self.export_class_third_filter_01_exhaust = self.value_class_third_filter_01_exhaust.get()
        self.export_size_third_filter_01_exhaust = self.value_size_third_filter_01_exhaust.get()
        self.export_quantity_third_filter_01_exhaust = self.value_quantity_third_filter_01_exhaust.get()
        self.export_symbol_third_filter_02_exhaust = self.value_symbol_third_filter_02_exhaust.get()
        self.export_class_third_filter_02_exhaust = self.value_class_third_filter_02_exhaust.get()
        self.export_size_third_filter_02_exhaust = self.value_size_third_filter_02_exhaust.get()
        self.export_quantity_third_filter_02_exhaust = self.value_quantity_third_filter_02_exhaust.get()
        self.export_heat_recovery = self.value_heat_recovery.get()
        self.export_glicol_symbol_motor_typ = self.value_glicol_symbol_motor_typ.get()
        self.export_glicol_motor_pwr = self.value_glicol_motor_pwr.get()
        self.export_glicol_motor_voltage = self.value_glicol_motor_voltage.get()
        self.export_rotor_exchanger_motor_pwr = self.value_rotor_exchanger_motor_pwr.get()
        self.export_rotor_exchanger_motor_voltage = self.value_rotor_exchanger_motor_voltage.get()
        self.export_humidifier_typ = self.value_humidifier_typ.get()
        self.export_humidifier_outgo = self.value_humidifier_outgo.get()
        self.export_humidifier_pwr = self.value_humidifier_pwr.get()
        self.export_humidifier_voltage = self.value_humidifier_voltage.get()
        self.export_humidifier_pump_typ = self.value_humidifier_pump_typ.get()
        self.export_humidifier_pump_current = self.value_humidifier_pump_current.get()
        self.export_humidifier_pump_pwr = self.value_humidifier_pump_pwr.get()
        self.export_humidifier_pump_voltage = self.value_humidifier_pump_voltage.get()
        self.export_aggregat_typ = self.value_aggregat_typ.get()
        self.export_voltage_aggregat = self.value_voltage_aggregat.get()
        self.export_start_current_aggregat = self.value_start_current_aggregat.get()
        self.export_max_current_aggregat = self.value_max_current_aggregat.get()
        self.export_mass = self.value_mass.get()

    # def print_2(self):
    #     # for i in range(len(self.a)):
    #     #     print(self.a[i])
    #
    #
    #     print (type(word))


    ######################################################################################################################

root = Tk()
root.title("DocHelper")
root.geometry("750x600")

tab_parent=ttk.Notebook(root)

tab_1= ttk.Frame(tab_parent)
tab_2= ttk.Frame(tab_parent)
tab_3= ttk.Frame(tab_parent)
tab_4= ttk.Frame(tab_parent)
tab_5= ttk.Frame(tab_parent)
tab_6= ttk.Frame(tab_parent)
tab_7= ttk.Frame(tab_parent)
tab_8= ttk.Frame(tab_parent)
tab_9= ttk.Frame(tab_parent)


tab_parent.add(tab_1,text='Identyfikacja')
tab_parent.add(tab_2,text='Nawiew')
tab_parent.add(tab_3,text='Wywiew')
tab_parent.add(tab_4,text='Nagrzewnice')
tab_parent.add(tab_5,text='Chłodnice')
tab_parent.add(tab_6,text='Nawiew - Filtry')
tab_parent.add(tab_7,text='Wywiew - Filtry')
tab_parent.add(tab_8,text='Odzysk')
tab_parent.add(tab_9,text='Pozostałe')


tab_parent.pack(expand=1,fill='both')


Label(tab_1,text="").pack()
Label(tab_2,text="").pack()
Label(tab_3,text="").pack()
Label(tab_4,text="").pack()
Label(tab_5,text="").pack()
Label(tab_6,text="").pack()
Label(tab_7,text="").pack()
Label(tab_8,text="").pack()
Label(tab_9,text="").pack()

app = Application(tab_parent)
root.mainloop()
