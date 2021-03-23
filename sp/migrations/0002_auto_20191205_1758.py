# Generated by Django 2.2.7 on 2019-12-05 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="idpattribute",
            options={
                "verbose_name": "attribute mapping",
                "verbose_name_plural": "attribute mappings",
            },
        ),
        migrations.AddField(
            model_name="idp",
            name="auth_case_sensitive",
            field=models.BooleanField(
                default=True, verbose_name="NameID is case sensitive"
            ),
        ),
        migrations.AddField(
            model_name="idp",
            name="create_users",
            field=models.BooleanField(
                default=True, verbose_name="Create users that do not already exist"
            ),
        ),
        migrations.AddField(
            model_name="idp",
            name="entity_id",
            field=models.CharField(
                blank=True,
                help_text="Leave blank to automatically use the metadata URL.",
                max_length=200,
                verbose_name="Entity ID",
            ),
        ),
        migrations.AddField(
            model_name="idpattribute",
            name="always_update",
            field=models.BooleanField(
                default=False,
                help_text=(
                    "Update this mapped user field on every successful authentication. "
                    "By default, mapped fields are only set on user creation."
                ),
                verbose_name="Always Update",
            ),
        ),
        migrations.AlterField(
            model_name="idp",
            name="base_url",
            field=models.CharField(
                help_text=(
                    "Root URL for the site, including http/https, no trailing slash."
                ),
                max_length=200,
                verbose_name="Base URL",
            ),
        ),
        migrations.CreateModel(
            name="IdPUserDefaultValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("field", models.CharField(max_length=200)),
                ("value", models.TextField()),
                (
                    "idp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_defaults",
                        to="sp.IdP",
                        verbose_name="identity provider",
                    ),
                ),
            ],
            options={
                "verbose_name": "user default value",
                "verbose_name_plural": "user default values",
                "unique_together": {("idp", "field")},
            },
        ),
    ]
