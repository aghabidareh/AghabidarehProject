// تابع برای تغییر بین لایت مود و دارک مود
document.getElementById("theme-toggle").addEventListener("click", function() {
    // اضافه کردن یا حذف کلاس light-mode از body
    document.body.classList.toggle("light-mode");

    // تغییر آیکون دکمه بر اساس تم فعلی
    const isLightMode = document.body.classList.contains("light-mode");
    this.textContent = isLightMode ? "🌙" : "🌞"; // تغییر آیکون از ماه به خورشید و برعکس
});
