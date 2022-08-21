from excel_manipulator import ExcelManipulator
import automation_bot
import time


def main():
    print("Program will start in 10 seconds. Please access \nhttps://www.zillow.com/how-much-is-my-home-worth/")
    time.sleep(10)
    start_time = None
    end_time = None
    dur = None
    manipulator = ExcelManipulator("xlsx_files\sample.xlsx", "Zestimate")
    adresses = manipulator.get_list_of_adresses()
    count = 1
    remaining = len(adresses)-1
    for adress in adresses:
        if end_time != None:
            dur = end_time-start_time
            decimals = "{: 2f}".format(dur)
            print(
                f"duration: {decimals} seconds, iteration {count} / {remaining}. ETA {int(dur*remaining/60)} mins")
            count += 1
            remaining -= 1
        start_time = time.time()
        estimate = automation_bot.get_the_estimate(adress)
        if estimate == "1234567890" or "N/A" in estimate:
            manipulator.estimates.append("N/A")
        else:
            manipulator.estimates.append(estimate[3:])
        end_time = time.time()

    manipulator.export_to_xlsx_file()


if __name__ == "__main__":
    main()
