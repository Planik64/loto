# Generated by Django 3.2.2 on 2021-05-21 08:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Резултат от мач', max_length=35)),
                ('type', models.CharField(choices=[('type_a', 'Резултат от мач'), ('type_b', 'Класиране в група'), ('type_c', 'Голмайстор'), ('type_d', 'Втори голмайстор'), ('type_e', 'Шампион'), ('type_f', 'Резултат от мач / Отбор победител'), ('type_g', 'Голмайстор брой голове')], default='type_a', max_length=35)),
                ('time_to_edit', models.DateTimeField()),
                ('is_result_a', models.BooleanField(default=False)),
                ('type_a_1_result', models.IntegerField(blank=True, null=True)),
                ('type_a_2_result', models.IntegerField(blank=True, null=True)),
                ('is_result_b', models.BooleanField(default=False)),
                ('type_b_1_result', models.IntegerField(blank=True, null=True)),
                ('type_b_2_result', models.IntegerField(blank=True, null=True)),
                ('type_b_3_result', models.IntegerField(blank=True, null=True)),
                ('type_b_4_result', models.IntegerField(blank=True, null=True)),
                ('is_result_c', models.BooleanField(default=False)),
                ('is_result_d', models.BooleanField(default=False)),
                ('is_result_e', models.BooleanField(default=False)),
                ('is_result_f', models.BooleanField(default=False)),
                ('type_f_1_result', models.IntegerField(blank=True, null=True)),
                ('type_f_2_result', models.IntegerField(blank=True, null=True)),
                ('is_result_g', models.BooleanField(default=False)),
                ('type_g_result', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Mybet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_a_bet_1', fernet_fields.fields.EncryptedIntegerField(default=0)),
                ('type_a_bet_2', fernet_fields.fields.EncryptedIntegerField(default=0)),
                ('type_b_bet_1', fernet_fields.fields.EncryptedIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('type_b_bet_2', fernet_fields.fields.EncryptedIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('type_b_bet_3', fernet_fields.fields.EncryptedIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('type_b_bet_4', fernet_fields.fields.EncryptedIntegerField(default=4, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('type_f_bet_1', fernet_fields.fields.EncryptedIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('type_f_bet_2', fernet_fields.fields.EncryptedIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('type_f_bet_3', models.CharField(default='', max_length=35)),
                ('type_g_bet_1', fernet_fields.fields.EncryptedIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('bet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loto_app.bet')),
                ('type_c_bet_1', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goalscorer', to='loto_app.player')),
                ('type_d_bet_1', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_goalscorer', to='loto_app.player')),
                ('type_e_bet_1', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='champion', to='loto_app.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bet',
            name='type_a_1_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_a_1', to='loto_app.team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_a_2_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_a_2', to='loto_app.team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_b_1_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_b_1', to='loto_app.team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_b_2_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_b_2', to='loto_app.team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_b_3_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_b_3', to='loto_app.team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_b_4_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_b_4', to='loto_app.team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_c_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_c_1', to='loto_app.player'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_d_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_d_1', to='loto_app.player'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_e_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_е_1', to='loto_app.team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_f_1_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_f_1', to='loto_app.team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_f_2_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_f_2', to='loto_app.team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='type_f_3_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_f_3', to='loto_app.team'),
        ),
    ]
