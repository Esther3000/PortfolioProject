select * from Portfolioproject. .covid_deaths$
order by 3,4

select * from Portfolioproject. .covid_vaccinations$
order by 3,4

select Location, date, total_cases, new_cases, total_deaths
from Portfolioproject. .covid_deaths$
order by 1,2


select Location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as Death_percentage
from Portfolioproject. .covid_deaths$
where location = 'Kenya'
order by 1,2
 
-- highest infection rate compared to population
select Location, MAX(total_cases) as highestInfectionCount, MAX((total_cases/population))*100 as percentage_pop_infected
from Portfolioproject. .CovidDeaths$
where continent is not null
group by Location, Population
order by percentage_pop_infected desc

--countries with highest deathcount per population
select Location, MAX(cast(total_deaths as int)) as highestDeathCount, MAX((total_deaths/population))*100 as percentage_pop_deaths
from Portfolioproject. .CovidDeaths$
where continent is not null
group by Location, Population
order by highestDeathCount desc

--highest death count by continent

select continent, MAX(cast(total_deaths as int)) as highestDeathCount
from Portfolioproject. .CovidDeaths$
where continent is not null
group by continent
order by highestDeathCount desc

--global numbers
select SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, (SUM(cast(new_deaths as int))/SUM(new_cases))*100 as percentage_new_cases
from Portfolioproject..CovidDeaths$
where continent is not null
group by date
order by 1,2

--total vaccinations vs population

with popvsvac (Continent, Location, Date, Population, New_vaccinations, RollingPeopleVaccinated)
as (
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
 SUM(CONVERT(int ,vac.new_vaccinations)) OVER (partition by dea.location, dea.date) as RollingPeopleVaccinated
from Portfolioproject..CovidDeaths$ dea
join Portfolioproject..covid_vaccinations$ vac
     on dea.location = vac.location
	 and dea.date = vac.date
where dea.continent is not null
--order by 2,3
)
select *, (RollingPeopleVaccinated/Population)*100 as RollingPeopleVaccinatedPercentage
from popvsvac


--temp table
   
DROP Table if exists PercentPopulationVaccinated
Create Table PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert into PercentPopulationVaccinated
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
 SUM(CONVERT(int ,vac.new_vaccinations)) OVER (partition by dea.location, dea.date) as RollingPeopleVaccinated
from Portfolioproject..CovidDeaths$ dea
join Portfolioproject..covid_vaccinations$ vac
     on dea.location = vac.location
	 and dea.date = vac.date
where dea.continent is not null
--order by 2,3
select *, (RollingPeopleVaccinated/Population)*100 as RollingPeopleVaccinatedPercentage
from PercentPopulationVaccinated



--creating view for later visualizations

Create view PercentPopVaccinated as 
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
 SUM(CONVERT(int ,vac.new_vaccinations)) OVER (partition by dea.location, dea.date) as RollingPeopleVaccinated
from Portfolioproject..CovidDeaths$ dea
join Portfolioproject..covid_vaccinations$ vac
     on dea.location = vac.location
	 and dea.date = vac.date
where dea.continent is not null
--order by 2,3







 
 


