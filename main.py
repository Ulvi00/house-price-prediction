import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

cedvel = pd.read_csv("evler.csv")

x = cedvel[["sahe", "otaq"]]
y = cedvel["qiymet"]


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)


model = LinearRegression()
model.fit(x_train, y_train)

test_texmini = model.predict(x_test)
mae = mean_absolute_error(y_test, test_texmini)

print(f"Test üzrə orta mütləq xəta (MAE): {mae:,.2f} AZN")


model.fit(x, y)

try:
    sahe = float(input("\nEvin sahəsini daxil et (m²): "))
    otaq = int(input("Otaq sayini daxil et: "))

    if sahe <= 0 or otaq <= 0:
        print("Sahə və otaq sayi müsbət olmalidir.")
    else:
        yeni_ev = pd.DataFrame({
            "sahe": [sahe],
            "otaq": [otaq]
        })

        texmin = model.predict(yeni_ev)[0]

        print(f"Təxmini ev qiyməti: {texmin:,.2f} AZN")


except ValueError:
    print("Sahəni rəqəm, otaq sayini isə tam ədəd kimi daxil et.")