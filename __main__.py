from excel_manipulator import ExcelManipulator
import automation_bot
import time


def main():
    st = None
    et = None
    dur = None
    manipulator = ExcelManipulator("xlsx_files\sample.xlsx", "Zestimate")
    adresses = manipulator.get_list_of_adresses()
    count = 1
    remaining = len(adresses)-1
    for adress in adresses:
        if et != None:
            dur = et-st
            decimals = "{: 2f}".format(dur)
            print(
                f"duration: {decimals} seconds, iteration {count} / {remaining}. ETA {int(dur*remaining/60)} mins")
            count += 1
            remaining -= 1
        st = time.time()
        estimate = automation_bot.get_the_estimate(adress)
        if estimate == "1234567890" or "N/A" in estimate:
            manipulator.estimates.append("N/A")
        else:
            manipulator.estimates.append(estimate[3:])
        # print(manipulator.estimates)
        et = time.time()
    manipulator.export_to_xlsx_file()


if __name__ == "__main__":
    main()
