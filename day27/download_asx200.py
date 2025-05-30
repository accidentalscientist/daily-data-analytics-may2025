import yfinance as yf

ticker     = "^AXJO"
start_date = "1992-11-22"
end_date   = "2025-06-05"

# fetch daily data
df = yf.download(
    ticker,
    start=start_date,
    end=end_date,
    interval="1d",
    auto_adjust=False
)

print(df.head())  # sanity check
df.to_csv("ASX200_full.csv")

