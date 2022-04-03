# Generated by Django 4.0.3 on 2022-04-03 17:32

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('header_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PostBlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='BlogPage',
            new_name='Blog',
        ),
        migrations.RemoveField(
            model_name='postpageblogcategory',
            name='page',
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='slug',
            field=models.SlugField(max_length=75, unique=True),
        ),
        migrations.RenameModel(
            old_name='PostPageTag',
            new_name='PostTag',
        ),
        migrations.DeleteModel(
            name='PostPage',
        ),
        migrations.DeleteModel(
            name='PostPageBlogCategory',
        ),
        migrations.AddField(
            model_name='postblogcategory',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='blog.blogcategory'),
        ),
        migrations.AddField(
            model_name='postblogcategory',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='blog.post'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='blog.PostTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='blog.post'),
        ),
    ]