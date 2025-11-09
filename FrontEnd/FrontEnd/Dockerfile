# === Runtime (ASP.NET 8) ===
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app

# === Build (SDK .NET 8) ===
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copia solo el csproj para cachear el restore
COPY FrontEnd/FrontEnd.csproj FrontEnd/
RUN dotnet restore FrontEnd/FrontEnd.csproj

# Copia el resto del repo
COPY . .
RUN dotnet publish FrontEnd/FrontEnd.csproj -c Release -o /app/publish /p:UseAppHost=false

# === Imagen final ===
FROM base AS final
WORKDIR /app
COPY --from=build /app/publish .

# Heroku te da $PORT; haz que Kestrel escuche ahí
CMD ["sh","-c","ASPNETCORE_URLS=http://0.0.0.0:${PORT} dotnet FrontEnd.dll"]
