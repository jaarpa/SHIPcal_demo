# Generated by Django 3.0.3 on 2020-06-25 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('simforms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlotVars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=5, verbose_name='Language')),
                ('Production_max', models.FloatField(verbose_name='Maximum production')),
                ('Production_lim', models.FloatField(verbose_name='Limited production')),
                ('Perd_term_anual', models.FloatField(verbose_name='Annual thermal losses')),
                ('DNI_anual_irradiation', models.FloatField(verbose_name='Annual irradiation')),
                ('Area', models.FloatField()),
                ('num_loops', models.IntegerField(verbose_name='Number of loops')),
                ('imageQlty', models.SmallIntegerField(verbose_name='Images quality')),
                ('plotPath', models.CharField(max_length=150, verbose_name='Plots path')),
                ('Energy_Before_annual', models.FloatField(verbose_name='Energy before boiler')),
                ('m_dot_min_kgs', models.FloatField(verbose_name='Minimum massic flux')),
                ('steps_sim', models.IntegerField(verbose_name='Simulation steps')),
                ('AmortYear', models.SmallIntegerField(verbose_name='Amortization year')),
                ('Selling_price', models.FloatField(verbose_name='Selling price')),
                ('in_s', models.FloatField(verbose_name='Inlet entropy')),
                ('out_s', models.FloatField(verbose_name='Outlet entropy')),
                ('T_in_flag', models.SmallIntegerField(verbose_name='Feeded from grid (0 no, 1 yes)')),
                ('Fuel_price', models.FloatField(verbose_name='Fuel price')),
                ('Boiler_eff', models.FloatField(verbose_name='Boiler efficiency')),
                ('T_in_C', models.FloatField(verbose_name='Inlet temperature towards collectors [C]')),
                ('T_out_C', models.FloatField(verbose_name='Outlet temperature from collectors [C]')),
                ('outProcess_s', models.FloatField(verbose_name='Outlet entropy from process')),
                ('T_out_process_C', models.FloatField(verbose_name='Outlet temperature from process')),
                ('P_op_bar', models.FloatField(verbose_name='Work pressure')),
                ('x_design', models.SmallIntegerField(verbose_name='Steam quality')),
                ('h_in', models.FloatField(verbose_name='Inlet enthalpy')),
                ('h_out', models.FloatField(verbose_name='Outlet enthalpy')),
                ('hProcess_out', models.FloatField(verbose_name='Inlet enthalpy towards process')),
                ('outProcess_h', models.FloatField(verbose_name='Outlet enthalpy from process')),
                ('sender', models.CharField(max_length=35, verbose_name='Sender')),
                ('type_integration', models.CharField(choices=[('SL_L_P', 'SL_L_P'), ('SL_L_PS', 'SL_L_PS'), ('SL_L_RF', 'SL_L_RF'), ('SL_L_DRF', 'SL_L_DRF'), ('SL_L_S', 'SL_L_S'), ('SL_L_S_PH', 'SL_L_S_PH'), ('SL_S_FW', 'SL_S_FW'), ('SL_S_FWS', 'SL_S_FWS'), ('SL_S_PD_OT', 'SL_S_PD_OT'), ('PL_E_PM', 'PL_E_PM'), ('SL_S_MW', 'SL_S_MW'), ('SL_S_MWS', 'SL_S_MWS'), ('SL_S_PD', 'SL_S_PD'), ('SL_S_PDS', 'SL_S_PDS')], max_length=20, verbose_name='Integration schema')),
                ('origin', models.SmallIntegerField(verbose_name='Origin')),
                ('n_years_sim', models.SmallIntegerField(verbose_name='Years simulated')),
                ('Break_cost', models.TextField(verbose_name='Break cost')),
                ('Acum_FCF', models.TextField(verbose_name='Acumulated FCF')),
                ('FCF', models.TextField()),
                ('T_in_C_AR', models.TextField(verbose_name='Water temperature from grid')),
                ('Demand', models.TextField(verbose_name='Demand')),
                ('Q_prod', models.TextField(verbose_name='Produced heat')),
                ('Q_prod_lim', models.TextField(verbose_name='Limited produced heat')),
                ('Q_charg', models.TextField(verbose_name='Charged heat')),
                ('Q_discharg', models.TextField(verbose_name='Discharged heat')),
                ('DNI', models.TextField(verbose_name='Solar radiation')),
                ('SOC', models.TextField()),
                ('Q_useful', models.TextField(verbose_name='Useful produced heat')),
                ('Q_defocus', models.TextField(verbose_name='Defocused heat')),
                ('T_alm_K', models.TextField(verbose_name='Storage temperature [k]')),
            ],
        ),
        migrations.CreateModel(
            name='ReportVars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=15, verbose_name='Version')),
                ('logo_output', models.CharField(max_length=150, verbose_name='Logo output')),
                ('type_integration', models.CharField(choices=[('SL_L_P', 'SL_L_P'), ('SL_L_PS', 'SL_L_PS'), ('SL_L_RF', 'SL_L_RF'), ('SL_L_DRF', 'SL_L_DRF'), ('SL_L_S', 'SL_L_S'), ('SL_L_S_PH', 'SL_L_S_PH'), ('SL_S_FW', 'SL_S_FW'), ('SL_S_FWS', 'SL_S_FWS'), ('SL_S_PD_OT', 'SL_S_PD_OT'), ('PL_E_PM', 'PL_E_PM'), ('SL_S_MW', 'SL_S_MW'), ('SL_S_MWS', 'SL_S_MWS'), ('SL_S_PD', 'SL_S_PD'), ('SL_S_PDS', 'SL_S_PDS')], max_length=20, verbose_name='Integration schema')),
                ('energyStored', models.IntegerField(verbose_name='Stored energy')),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('Area_total', models.FloatField(verbose_name='Total area')),
                ('n_coll_loop', models.IntegerField(verbose_name='Collectors per loop')),
                ('energStorageMax', models.IntegerField(verbose_name='Max stored energy')),
                ('num_loops', models.IntegerField(verbose_name='Number of loops')),
                ('m_dot_min_kgs', models.FloatField(verbose_name='Minimum massic flux')),
                ('Production_max', models.FloatField(verbose_name='Maximum production')),
                ('Production_lim', models.FloatField(verbose_name='Limited production')),
                ('Demand_anual', models.FloatField(verbose_name='Annual demand')),
                ('solar_fraction_max', models.FloatField(verbose_name='Maximum solar fraction')),
                ('solar_fraction_lim', models.FloatField(verbose_name='Limited solar fraction')),
                ('DNI_anual_irradiation', models.FloatField(verbose_name='Annual irradiation')),
                ('AmortYear', models.SmallIntegerField(verbose_name='Amortization year')),
                ('finance_study', models.SmallIntegerField(verbose_name='Requested finance study (0 no, 1 yes)')),
                ('CO2', models.SmallIntegerField(verbose_name='CO2 flag')),
                ('co2Savings', models.FloatField(verbose_name='Savings from CO2')),
                ('TIRscript', models.CharField(max_length=30, verbose_name='IRR text')),
                ('TIRscript10', models.CharField(max_length=40, verbose_name='IRR10 text')),
                ('Amortscript', models.CharField(max_length=40, verbose_name='Amortization text')),
                ('co2TonPrice', models.FloatField(verbose_name='Price per CO2 Ton')),
                ('fuelIncremento', models.FloatField(verbose_name='Fuel increase')),
                ('IPC', models.FloatField()),
                ('Selling_price', models.FloatField(verbose_name='Selling price')),
                ('IRR', models.FloatField(verbose_name='IRR')),
                ('IRR10', models.FloatField(verbose_name='IRR 10')),
                ('tonCo2Saved', models.FloatField(verbose_name='CO2 saved Tons')),
                ('LCOE', models.FloatField(verbose_name='Levelized cost of energy')),
                ('Energy_savings_mean', models.FloatField(verbose_name='Mean energy savings')),
                ('lang', models.CharField(max_length=5, verbose_name='Language')),
                ('sender', models.CharField(max_length=35, verbose_name='Sender')),
                ('cabecera', models.CharField(max_length=40, verbose_name='Report header')),
                ('mapama', models.SmallIntegerField()),
                ('totalCharged', models.FloatField(verbose_name='Total charged energy')),
                ('totalDischarged', models.FloatField(verbose_name='Total discharged energy')),
                ('totalDefocus', models.FloatField(verbose_name='Total defocused energy')),
                ('improvStorage', models.FloatField()),
                ('Utilitation_ratio', models.FloatField(verbose_name='Utilization ratio')),
                ('flowrate_kgs_average', models.FloatField(verbose_name='Mean massic flux')),
                ('Energy_module_max', models.FloatField(verbose_name='Max energy produced per module')),
                ('mofINV', models.IntegerField(verbose_name='Investment modificator')),
                ('mofDNI', models.IntegerField(verbose_name='Irradiation modificator')),
                ('mofProd', models.IntegerField(verbose_name='Production modificator')),
                ('fraction_savings', models.FloatField(verbose_name='Mean savings')),
                ('fuelPrizeArrayList', models.TextField(verbose_name='Yearly fuel price')),
                ('Acum_FCFList', models.TextField(verbose_name='Acumulated FCF')),
                ('Energy_savingsList', models.TextField(verbose_name='Energy savings')),
                ('OM_cost_year', models.TextField(verbose_name='Operation and maniteinance annual costs')),
                ('anual_energy_cost', models.TextField(verbose_name='Annual energy costs')),
                ('Q_prod', models.TextField(verbose_name='Produced heat')),
                ('Q_prod_lim', models.TextField(verbose_name='Limited produced heat')),
                ('Demand', models.TextField(verbose_name='Annual demand')),
                ('Q_charg', models.TextField(verbose_name='Charged heat')),
                ('Q_discharg', models.TextField(verbose_name='Discharged heat')),
                ('Q_defocus', models.TextField(verbose_name='Defocused heat')),
                ('flow_rate_kgs', models.TextField(verbose_name='Massic flows')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateVars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v', models.CharField(max_length=15, verbose_name='Version')),
            ],
        ),
        migrations.CreateModel(
            name='SimResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=15, verbose_name='Version')),
                ('plotVars', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='results.PlotVars')),
                ('reportsVar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='results.ReportVars')),
                ('simulation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='simforms.Simulation')),
                ('templateVars', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='results.TemplateVars')),
            ],
        ),
    ]
