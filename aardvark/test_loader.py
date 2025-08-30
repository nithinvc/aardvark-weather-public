from loader import WeatherDatasetE2E


def test_loader():
    lead_time = 24
    dataset = WeatherDatasetE2E(
        device="cuda",
        hadisd_mode="train",
        start_date="2021-01-01",
        end_date="2021-12-10",
        lead_time=lead_time,
        era5_mode="4u",
        mode="train",
        hadisd_var="tas",
        data_path="/mnt/local_storage/weather/aardvark/aardvark/training_data_interpolated/",
        aux_data_path="../data-constants/",
    )


if __name__ == "__main__":
    test_loader()